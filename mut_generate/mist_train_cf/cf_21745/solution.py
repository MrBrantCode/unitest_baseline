"""
QUESTION:
Create a function called `determine_age_group` that takes in a Pandas DataFrame with an 'Age' column and adds a new column 'age_group' based on the following age ranges: "young" for ages less than 25, "middle-aged" for ages between 25 and 55 (inclusive), and "elderly" for ages greater than 55. The solution should be efficient, aiming for a time complexity of O(n), where n is the number of rows in the DataFrame.
"""

import pandas as pd

def determine_age_group(df):
    """
    This function takes in a Pandas DataFrame with an 'Age' column and adds a new column 'age_group' 
    based on the following age ranges: "young" for ages less than 25, "middle-aged" for ages between 
    25 and 55 (inclusive), and "elderly" for ages greater than 55.

    Args:
        df (pd.DataFrame): A DataFrame with an 'Age' column.

    Returns:
        pd.DataFrame: The input DataFrame with an additional 'age_group' column.
    """

    def age_group(age):
        if age < 25:
            return 'young'
        elif age >= 25 and age <= 55:
            return 'middle-aged'
        else:
            return 'elderly'

    df['age_group'] = df['Age'].apply(age_group)
    return df