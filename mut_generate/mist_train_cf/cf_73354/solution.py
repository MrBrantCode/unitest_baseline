"""
QUESTION:
Create a function `json_to_dataframe` that takes a list of JSON objects as input and returns a Pandas dataframe. The function should handle any missing or null values by replacing them with a default value, and ensure that there are no duplicate entries in the resulting dataframe.
"""

import pandas as pd

def json_to_dataframe(json_objects, default_value='Unknown'):
    """
    Converts a list of JSON objects into a Pandas DataFrame, handling missing or null values and removing duplicates.

    Args:
    json_objects (list): A list of JSON objects.
    default_value (str): The default value to replace missing or null values. Defaults to 'Unknown'.

    Returns:
    pd.DataFrame: A Pandas DataFrame constructed from the input JSON objects.
    """
    df = pd.DataFrame(json_objects)
    df.fillna(default_value, inplace=True)
    df.drop_duplicates(inplace=True)
    return df