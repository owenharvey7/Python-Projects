"""
# 10
# File Handling Challenge:
# Read data from a CSV file and print it in a structured way.
# Difficulty: Medium
"""

# import pandas to read the CSV file
import pandas as pd

# read the CSV file
data = pd.read_csv('Python CSV Practice File.csv')

print("This program reads a CSV file and prints out the data.\n\n")


# print the data in a structured way
print(data.to_string())






