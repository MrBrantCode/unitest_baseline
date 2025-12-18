"""
QUESTION:
Create a function called `clean_data` that takes a pandas DataFrame as input. The function should replace all NaN and None values in the DataFrame with 0. The function should return the cleaned DataFrame. The function does not take any other parameters besides the input DataFrame.
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces all NaN and None values in the DataFrame with 0.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df.fillna(0, inplace=True)
    return df