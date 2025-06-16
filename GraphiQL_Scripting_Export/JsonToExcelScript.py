import json
import pandas as pd

## This script processes a JSON file containing data sources and flows, extracting relevant information and saving it to an Excel file.

# Define file paths
input_file = 'SampleData.json'  # Update with your actual JSON file
output_file = "DataSources.xlsx"

# Load the filtered JSON data
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract relevant fields for the DataFrame
datasources_list = []

# Iterate through each tag in the tags array
for tag in data["data"]["tags"]:
    # Process publishedDatasources
    for ds in tag["publishedDatasources"]:
        ds_id = ds.get("id", "N/A")
        name = ds.get("name", "N/A")
        # Extract tag names as a comma-separated string
        tag_names = ", ".join(t.get("name", "N/A") for t in ds.get("tags", []))
        datasources_list.append({
            "Type": "DataSource",
            "Name": name,
            "ID": ds_id,
            "Tags": tag_names
        })
    
    # Process flows
    for flow in tag["flows"]:
        flow_id = flow.get("id", "N/A")
        name = flow.get("name", "N/A")
        # Extract tag names as a comma-separated string
        tag_names = ", ".join(t.get("name", "N/A") for t in flow.get("tags", []))
        datasources_list.append({
            "Type": "Flow",
            "Name": name,
            "ID": flow_id,
            "Tags": tag_names
        })

# Create a DataFrame
df = pd.DataFrame(datasources_list, columns=["Type", "Name", "ID", "Tags"])

# Save to Excel
df.to_excel(output_file, index=False)

print(f"Excel file saved as {output_file}")