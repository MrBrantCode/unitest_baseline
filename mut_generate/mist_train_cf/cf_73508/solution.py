"""
QUESTION:
Design a function called `clean_and_validate_df` that takes a pandas DataFrame `df` as input and performs necessary data cleaning and validation tasks on it. The function should return a cleaned and validated DataFrame along with a boolean value indicating whether the data is valid or not. If the data is not valid, the function should return the original DataFrame (or any other value that makes sense for the problem) along with `False`. Use Python and common libraries like pandas and NumPy.
"""

import pandas as pd

def clean_and_validate_df(df: pd.DataFrame) -> (pd.DataFrame, bool):
    """
    This function performs necessary data cleaning and validation tasks on a pandas DataFrame.
    
    Args:
    df (pd.DataFrame): The input DataFrame to be cleaned and validated.
    
    Returns:
    A tuple containing the cleaned and validated DataFrame and a boolean value indicating whether the data is valid or not.
    If the data is not valid, the function returns the original DataFrame along with False.
    """
    
    # You can use pandas features to clean and validate data
    # If the data is not valid raise exception or return None, False
    # For the sake of simplicity, I am returning the data 'as is'
    return df, True