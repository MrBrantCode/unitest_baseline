"""
QUESTION:
Write a function `convert_to_dataframe` that takes a nested list of dictionaries as input and returns a Pandas DataFrame. The function should filter out entries with missing values and only include columns with unique values. The function should also sort the columns in alphabetical order.
"""

import pandas as pd

def convert_to_dataframe(nested_list):
    """
    Converts a nested list of dictionaries into a Pandas DataFrame while filtering out entries with missing values 
    and only including columns with unique values
    
    Parameters:
    -----------
    nested_list : list of dictionaries
        The nested list of dictionaries
    
    Returns:
    --------
    pd.DataFrame
        The resulting Pandas DataFrame
    """
    columns = set()
    for dictionary in nested_list:
        columns = columns.union(set(dictionary.keys()))

    columns = list(columns)
    columns.sort()

    filtered_list = []
    for dictionary in nested_list:
        filtered_dict = {}
        for column in columns:
            if column in dictionary and dictionary[column] is not None:
                filtered_dict[column] = dictionary[column]
        if len(filtered_dict) == len(columns):
            filtered_list.append(filtered_dict)

    return pd.DataFrame(filtered_list, columns=columns)