"""
QUESTION:
Create a function called `create_dataframe` that takes a dictionary as input and returns a Pandas DataFrame. The dictionary keys should be used as column names and the corresponding values should be lists containing the data for each column.
"""

import pandas as pd

def create_dataframe(data):
    """
    Creates a Pandas DataFrame from a dictionary.

    Args:
        data (dict): A dictionary where keys are column names and values are lists containing the data for each column.

    Returns:
        pd.DataFrame: A Pandas DataFrame created from the input dictionary.
    """
    return pd.DataFrame(data)