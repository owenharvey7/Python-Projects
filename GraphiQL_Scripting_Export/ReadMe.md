# GraphiQL Scripting

## The purpose of this project is to export Datasources and Flows from Tableau using GraphiQL and then take the data and put it in an Excel file to convert data sources

### How to Use:
1. Open up the Tableau client.
2. Navigate to External Assets.
3. Open Query metadata (GraphiQL) in the top right corner.
4. Dump in the GraphiQL_Query file (The file will retrieve all data sources and flows with a specific tag).
5. CTL + A the results and dump them into the SampleData file (or make your own .json file).
6. Open up the JsonToExcelScript and run it. Make sure it's pulling from your .json file.
7. This should export to an Excel file where you can sort and manipulate the tables for a given purpose. 
