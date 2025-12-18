"""
QUESTION:
Create a function named `analyze_csv` that takes a CSV file path as input, loads the file into a pandas DataFrame, and provides methods to analyze the data. The function should include methods to display the top and bottom rows, column names, a summary of numerical information, and data types of each column. The function should be implemented using the pandas library in Python.
"""

import pandas as pd

def analyze_csv(csv_file_path):
    """
    Analyze a CSV file using pandas DataFrame.
    
    Parameters:
    csv_file_path (str): Path to the CSV file.
    
    Returns:
    df (DataFrame): A pandas DataFrame containing the CSV data.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Display the top rows
    print("Top Rows:")
    print(df.head())
    
    # Display the bottom rows
    print("\nBottom Rows:")
    print(df.tail())
    
    # Display column names
    print("\nColumn Names:")
    print(df.columns)
    
    # Display a summary of numerical information
    print("\nNumerical Information Summary:")
    print(df.describe())
    
    # Display data types of each column
    print("\nData Types of Each Column:")
    print(df.info())
    
    return df