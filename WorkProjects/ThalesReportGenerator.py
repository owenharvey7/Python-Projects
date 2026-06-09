import requests
import time
import os
import sys
import json
import base64
from datetime import datetime, timedelta
from urllib.parse import urlparse

# --- Configuration ---
# Sensitive values loaded from environment variables.
# Set these before running:
#   API_BASE_URL, API_USERNAME, API_PASSWORD, REPORT_ID, OUTPUT_DIR
API_BASE_URL = os.environ.get('API_BASE_URL', 'https://your-sentinel-instance.example.com')
USERNAME = os.environ.get('API_USERNAME')
PASSWORD = os.environ.get('API_PASSWORD')
REPORT_ID = os.environ.get('REPORT_ID')
OUTPUT_DIR = os.environ.get('OUTPUT_DIR', r'C:\path\to\output')

# Validate required environment variables
_missing = [k for k, v in {'API_USERNAME': USERNAME, 'API_PASSWORD': PASSWORD, 'REPORT_ID': REPORT_ID}.items() if not v]
if _missing:
    print(f"Error: Missing required environment variables: {', '.join(_missing)}")
    sys.exit(1)

# Set to generate report, but can also list reports
MODE = 'generate'

# The end date is set to yesterday's date.
# Add - timedelta(days=1) to make the end date, the previous day
end_date = datetime.now()

# The start date is set to January 1st of the current year.
start_date = datetime(end_date.year, 1, 1)

# Set variables
REPORT_START_DATE = start_date.strftime("%Y-%m-%d")
REPORT_END_DATE = end_date.strftime("%Y-%m-%d")

# Polling configuration for checking job status.
POLLING_INTERVAL = 10
MAX_POLLING_ATTEMPTS = 60

# --- API Endpoints ---
GENERATE_REPORT_ENDPOINT = f'{API_BASE_URL}/ems/api/v5/reportTemplates/{REPORT_ID}/generateReport'
REPORT_TEMPLATES_ENDPOINT = f'{API_BASE_URL}/ems/api/v5/reportTemplates'
JOB_STATUS_ENDPOINT = f'{API_BASE_URL}/ems/api/v5/reportJobs'


# --- Utility Functions ---

def get_auth_headers():
    """Generates the Authorization header for Basic Authentication."""
    credentials = f"{USERNAME}:{PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return {'Authorization': f'Basic {encoded_credentials}'}

def list_reports():
    """Fetches and prints a list of all available report templates."""
    print("Fetching list of available report templates...")
    headers = get_auth_headers()
    
    try:
        response = requests.get(REPORT_TEMPLATES_ENDPOINT, headers=headers)
        response.raise_for_status()
        
        reports_data = response.json()
        
        if not reports_data.get('reports'):
            print("No reports found or the 'reports' key is missing from the response.")
            return

        print("\nAvailable Report Templates:")
        print("-" * 75)
        for report in reports_data['reports']:
            report_name = report.get('name')
            report_id = report.get('id')
            if report_name and report_id:
                print(f"Name: {report_name:<50} | ID: {report_id}")
        print("-" * 75)
        print("\nCopy the ID and paste it into the REPORT_ID variable. Then set MODE to 'generate'.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching report list: {e}")
    except json.JSONDecodeError:
        print(f"Error: Non-JSON response received. Response was: {response.text}")


def trigger_report_generation(report_start_date, report_end_date):
    """Triggers the report generation job and returns the job URL."""
    print(f"Report job triggered for report ID: {REPORT_ID}...")
    headers = get_auth_headers()
    
    payload = {
        "reportType": "csv",
        "StartDate": report_start_date,
        "EndDate": report_end_date
    }
    
    try:
        response = requests.post(GENERATE_REPORT_ENDPOINT, headers=headers, params=payload, allow_redirects=False)
        response.raise_for_status()
        
        job_url = response.headers.get('Location')
        if not job_url:
            print("Failed to get job URL from 'Location' header.")
            return None
            
        return job_url
        
    except requests.exceptions.RequestException as e:
        print(f"Error triggering report: {e}")
        return None

def check_job_status(job_id):
    """Checks the status of a specific job ID and returns the job data."""
    headers = get_auth_headers()
    url = f'{JOB_STATUS_ENDPOINT}/{job_id}'
    params = {'getDownloadUrl': 'true'}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        job_data = response.json()
        return job_data
    except requests.exceptions.RequestException as e:
        print(f"Error checking job status: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Non-JSON response received while checking job status. Response was: {response.text}")
        return None

def poll_for_report_completion(job_url):
    """Polls the report job URL until the report is ready for download."""
    print("Waiting for report generation to complete...")
    job_id = os.path.basename(job_url)
    
    for attempt in range(1, MAX_POLLING_ATTEMPTS + 1):
        job_status = check_job_status(job_id)
        if not job_status:
            return None
        
        status = job_status.get('reportJob', {}).get('state')
        
        if status == 'COMPLETED':
            download_url = job_status.get('reportJob', {}).get('downloadUrl')
            if not download_url:
                print("Report job is complete, but no download URL found.")
                return None
            print("Report job is complete!")
            return download_url
        
        if status == 'FAILED':
            print("Report generation failed on the server.")
            return None
            
        time.sleep(POLLING_INTERVAL)
            
    print("Maximum polling attempts reached. Giving up.")
    return None

def download_report(download_url, output_path):
    """Downloads the report from the given URL and saves it to a file."""
    print("Beginning download...")
    headers = get_auth_headers()
    
    try:
        response = requests.get(download_url, headers=headers, stream=True)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    
        print(f"Report successfully downloaded and saved to {output_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading report: {e}")
        return False

# --- Main Script Logic ---
if __name__ == "__main__":
    if MODE == 'list':
        list_reports()
    elif MODE == 'generate':
        report_job_url = trigger_report_generation(REPORT_START_DATE, REPORT_END_DATE)
        if not report_job_url:
            sys.exit(1)
            
        report_download_url = poll_for_report_completion(report_job_url)
        if not report_download_url:
            sys.exit(1)

        # The output filename now reflects the "Year to Date" range
        output_filename = f'ThalesReport_YTD_{end_date.year}.csv' # This allows for years to not get overwritten
        output_filepath = os.path.join(OUTPUT_DIR, output_filename)
        
        if not download_report(report_download_url, output_filepath):
            print("Failed to download the final report.")
            sys.exit(1)
            
        print("\nScript completed successfully.")
    else:
        print(f"Invalid mode: {MODE}. Please set MODE to 'list' or 'generate'.")
        sys.exit(1)
