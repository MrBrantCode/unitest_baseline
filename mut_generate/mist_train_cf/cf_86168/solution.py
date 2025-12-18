"""
QUESTION:
Develop a function named `process_data` that takes a multi-dimensional dataset containing numbers and strings with missing values, checks for type inconsistency, and fills missing values. The function should be able to handle both numerical and categorical columns. Implement error handling to ensure the input is a pandas DataFrame.
"""

import pandas as pd
import numpy as np

def process_data(info):
    """
    Processes a dataset. 
    Checks for type inconsistency and fills missing (null) values.
    
    Parameters:
    info (DataFrame): Pandas DataFrame containing the dataset
    
    Returns:
    DataFrame: Processed DataFrame
    """
    try:
        assert isinstance(info, pd.DataFrame)
    except AssertionError:
        return "Error: Dataset must be a pandas DataFrame"
        
    for col in info.columns:
        if info[col].dtypes == "object": # If it is categorical column
            fill_value = info[col].mode().iloc[0]  
        else: # If it's numerical column
            fill_value = info[col].mean()
            
        info[col] = info[col].fillna(fill_value)
        
    return info