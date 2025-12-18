"""
QUESTION:
Create a function named `create_dataframe` that takes a list of tuples as input, where each tuple contains an integer and a dictionary with a single key-value pair. The function should return a pandas DataFrame with two columns: 'Key' and 'Value'. The 'Key' column should contain the integer from each tuple, and the 'Value' column should contain the dictionary value from each tuple.
"""

import pandas as pd

def create_dataframe(data):
    keys = [i[0] for i in data]
    values = [list(i[1].values())[0] for i in data]
    return pd.DataFrame(list(zip(keys, values)), columns =['Key', 'Value'])