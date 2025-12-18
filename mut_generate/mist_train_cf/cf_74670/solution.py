"""
QUESTION:
Write a function `csv_to_list(csv_file)` that takes a CSV file path as input, reads the file into a pandas DataFrame, performs basic data transformations, and converts the DataFrame into a Python list of lists where each sub-list represents a row of data. The function should handle any possible exceptions that can occur during the reading, transformation, and conversion of the data.
"""

import pandas as pd

def csv_to_list(csv_file):
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error occurred while reading CSV file: {e}")
        return 
    
    try:
        transformed_df = df.copy()
    except Exception as e:
        print(f"Error occurred while transforming data: {e}")
        return 

    try:
        data_list = transformed_df.values.tolist()
    except Exception as e:
        print(f"Error occurred while converting DataFrame to list: {e}")
        return
    
    return data_list