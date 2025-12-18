"""
QUESTION:
Create a function `create_dataframe` that returns a pandas DataFrame with columns 'A', 'B', and 'C'. The function should be able to take in three lists of integers as parameters. The returned DataFrame should have the values from the input lists as its column values. Each list should correspond to a column in the resulting DataFrame, and the order of the values in the lists should be preserved in the DataFrame. The input lists should be of the same length.
"""

import pandas as pd

def create_dataframe(list_A, list_B, list_C):
    return pd.DataFrame({"A": list_A, "B": list_B, "C": list_C})