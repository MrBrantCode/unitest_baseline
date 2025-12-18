"""
QUESTION:
Create a function `create_dataframe` that generates a pandas DataFrame with a specified number of rows. The DataFrame should contain an index column and a 'Dummy' column filled with ones. The index column should be set as the DataFrame's index. The function should take the number of rows as input and return the generated DataFrame.
"""

import pandas as pd

def create_dataframe(n):
    """
    Generates a pandas DataFrame with a specified number of rows.
    
    Parameters:
    n (int): The number of rows in the DataFrame.
    
    Returns:
    pandas.DataFrame: A DataFrame with an index column and a 'Dummy' column filled with ones.
    """
    df = pd.DataFrame({'Index': range(1, n+1), 'Dummy': 1})
    df.set_index('Index', inplace=True)
    return df