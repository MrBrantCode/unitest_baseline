"""
QUESTION:
Write a function `average_software_engineer_age` that takes a pandas DataFrame with columns 'age' and 'job_title' as input, calculates the average age of individuals with a job title of 'Software Engineer', and returns the average age if it exceeds 35 years.
"""

import pandas as pd

def average_software_engineer_age(df):
    """
    This function calculates the average age of individuals with a job title of 'Software Engineer' 
    in a given DataFrame and returns the average age if it exceeds 35 years.

    Args:
        df (pd.DataFrame): A pandas DataFrame with columns 'age' and 'job_title'.

    Returns:
        float or None: The average age of 'Software Engineer' if it's greater than 35, otherwise None.
    """

    # Filter the DataFrame to include only rows where the job title is 'Software Engineer'
    filtered_df = df.loc[df['job_title'] == 'Software Engineer']
    
    # Calculate the average age of the filtered DataFrame
    average_age = filtered_df['age'].mean()
    
    # Return the average age if it exceeds 35 years
    return average_age if average_age > 35 else None