"""
QUESTION:
Replace all negative values in a Pandas dataframe with a given string. The function should accept a Pandas dataframe as input and a string value to replace the negative values. Negative values are considered as those less than zero and can be of either integer or float data type.
"""

import pandas as pd

def replace_negative_values(df, replacement):
    """
    Replace all negative values in a pandas dataframe with a given string.

    Args:
    df (pd.DataFrame): Input dataframe.
    replacement (str): String to replace negative values.

    Returns:
    pd.DataFrame: Dataframe with negative values replaced.
    """
    return df.applymap(lambda x: replacement if isinstance(x, (int, float)) and x < 0 else x)