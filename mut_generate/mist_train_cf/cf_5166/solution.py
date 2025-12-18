"""
QUESTION:
Create a function named `filter_dataframe` that filters a given pandas DataFrame. The function should return rows where the 'name' is not null, 'age' is greater than 30, 'salary' is between 50000 and 100000, 'department' is not null, and 'years_of_experience' is greater than or equal to 5.
"""

import pandas as pd

def filter_dataframe(df):
    """
    Filter a pandas DataFrame based on specific conditions.

    Parameters:
    df (pd.DataFrame): The DataFrame to be filtered.

    Returns:
    pd.DataFrame: A filtered DataFrame where 'name' is not null, 'age' is greater than 30, 
                  'salary' is between 50000 and 100000, 'department' is not null, and 
                  'years_of_experience' is greater than or equal to 5.
    """
    mask_name = df['name'].notnull()
    mask_age = df['age'] > 30
    mask_salary = df['salary'].between(50000, 100000)
    mask_department = df['department'].notnull()
    mask_years_of_experience = df['years_of_experience'] >= 5
    
    return df[mask_name & mask_age & mask_salary & mask_department & mask_years_of_experience]