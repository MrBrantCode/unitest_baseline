"""
QUESTION:
Create a pandas DataFrame from a dictionary with 'state', 'year', and 'pop' information. The dictionary should have these keys with corresponding list values. Implement the function `create_dataframe()` that takes a dictionary as input and returns a pandas DataFrame. The function should not take any additional parameters.
"""

import pandas as pd

def create_dataframe(data_dict):
    """
    Create a pandas DataFrame from a dictionary.

    Parameters:
    data_dict (dict): A dictionary with lists as values.

    Returns:
    pd.DataFrame: A pandas DataFrame.
    """
    return pd.DataFrame(data_dict)