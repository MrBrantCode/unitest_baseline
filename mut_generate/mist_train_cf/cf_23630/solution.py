"""
QUESTION:
Write a function named `explore_dataset` to efficiently explore a large dataset using the Pandas library. The function should take a CSV file path as input and return a summary of the dataset, including the first few rows, last few rows, information about the dataset, and a statistical description of the data. The function should use Pandas' built-in methods such as head(), tail(), info(), and describe().
"""

import pandas as pd

def explore_dataset(csv_file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Get the first few rows of the dataset
        first_rows = df.head()
        
        # Get the last few rows of the dataset
        last_rows = df.tail()
        
        # Get information about the dataset
        info = df.info()
        
        # Get a statistical description of the data
        description = df.describe()
        
        # Return the results
        return first_rows, last_rows, info, description
    
    except Exception as e:
        return f"An error occurred: {str(e)}"