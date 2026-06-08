#Query Datas from SAP Datasphere using SQL. Has multipurpose uses, but this is just the base function 
import pyodbc
import pandas as pd

#General Connection Details
HOST     = "DataSphere Host Name"
PORT     = 'Port Number'
USER     = "Generic UserName"
PASSWORD = "Password"

#Connection String
connection_string = (
    f"DRIVER={{HDBODBC}};"
    f"SERVERNODE={HOST}:{PORT};"
    f"UID={USER};"
    f"PWD={{{PASSWORD}}};"
    f"encrypt=true;"
    f"sslValidateCertificate=false;"
)

#SQL Query
sql = """
    SELECT * FROM "Space"."Object"
    WHERE "Condition" = 'Value'
"""

try:
    #Connect
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    #Execute SQL
    cursor = conn.cursor()
    cursor.execute(sql)

    #Store SQL
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    #Display SQL 
    df = pd.DataFrame.from_records(rows, columns=columns)
    print(df)

    #Exit/Close
    cursor.close()
    conn.close()

#Catch clause for errors, displays error message
except pyodbc.Error as e:
    print(f"Query failed: {e}")
