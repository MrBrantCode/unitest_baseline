"""
QUESTION:
Implement the `load_csv` function to load property tax data from a CSV file and return it as a pandas DataFrame. The function should take the path to the CSV file as an argument. The `load_csv` function will be used to process property tax data for the years 2006 to 2015.
"""

import pandas as pd

def load_csv(file_path):
    """
    Load property tax data from a CSV file and return it as a DataFrame.

    Args:
    file_path (str): The path to the CSV file containing property tax data.

    Returns:
    pd.DataFrame: DataFrame containing the property tax data.
    """
    return pd.read_csv(file_path)