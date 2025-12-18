"""
QUESTION:
Create a function named `construct_dataframe` that constructs a pandas DataFrame from the given data, handles any missing values by replacing them with 0, and ensures the 'Years' column contains only integer values. The function should take a dictionary with 'Person', 'Years', and 'Country' as keys and corresponding values as input.
"""

import pandas as pd
import numpy as np

def construct_dataframe(data):
    """
    Construct a pandas DataFrame from the given data, handle any missing values 
    by replacing them with 0, and ensure the 'Years' column contains only integer values.

    Parameters:
    data (dict): A dictionary with 'Person', 'Years', and 'Country' as keys and 
                 corresponding values.

    Returns:
    pandas DataFrame
    """
    df = pd.DataFrame(data)
    df['Years'] = df['Years'].fillna(0).astype(int)
    return df