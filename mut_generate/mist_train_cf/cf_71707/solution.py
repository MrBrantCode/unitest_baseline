"""
QUESTION:
Write a function named `parse_data` that takes a string of CSV data as input and returns a pandas DataFrame. The function should parse the CSV data into a DataFrame without using pandas' built-in functionality for reading CSV files. The function should be robust enough to handle potential errors in the CSV file structure, including lines with an incorrect number of fields. The first line of the CSV data is assumed to be the header row.
"""

import pandas as pd

def parse_data(csv_data):
    try:
        lines = csv_data.split("\n")
        headers = lines[0].split(",")
        data = []

        for line in lines[1:]:
            fields = line.split(",")
            if len(fields) != len(headers):
                print("Skipping line due to incorrect number of fields: ", line)
                continue
            data.append(fields)
        return pd.DataFrame(data, columns = headers)
    except Exception as e:
        print("Error in parsing CSV data into a DataFrame: ", e)