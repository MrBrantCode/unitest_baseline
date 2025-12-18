"""
QUESTION:
Create a function `construct_dataframe` that takes a list of tuples as input, where each tuple contains an integer and a dictionary. The function should return a Pandas DataFrame where the dictionaries are used to create the DataFrame's columns and the integers are used as the index. The data types of the dictionary values should be preserved.
"""

import pandas as pd

def construct_dataframe(data):
    """
    Construct a Pandas DataFrame from a list of tuples.
    
    Parameters:
    data (list): A list of tuples, where each tuple contains an integer and a dictionary.
    
    Returns:
    pd.DataFrame: A Pandas DataFrame where the dictionaries are used to create the DataFrame's columns and the integers are used as the index.
    """
    df = pd.DataFrame([b for a, b in data])
    df.index = [a for a, b in data]
    return df