"""
QUESTION:
Create a function called categorize_ages that takes a pandas DataFrame as input. The DataFrame should have an 'Age' column. The function should do the following: 
- Remove all rows from the DataFrame where 'Age' is negative.
- Sort the remaining rows in descending order by 'Age'.
- Add a new 'Category' column to the DataFrame, where 'Category' is assigned as follows:
    - 'Child' if 'Age' is between 0 and 18 (inclusive)
    - 'Adult' if 'Age' is between 19 and 65 (inclusive)
    - 'Senior' if 'Age' is above 65.
"""

import pandas as pd

def categorize_ages(df):
    """
    This function takes a pandas DataFrame as input, removes rows with negative 'Age', 
    sorts the remaining rows in descending order by 'Age', and assigns a 'Category' 
    based on the 'Age' range.

    Args:
    df (pd.DataFrame): A pandas DataFrame with an 'Age' column.

    Returns:
    pd.DataFrame: The modified DataFrame with 'Category' column added.
    """

    # Remove rows with negative 'Age'
    df = df[df['Age'] >= 0]
    
    # Sort the remaining rows in descending order by 'Age'
    df = df.sort_values(by='Age', ascending=False)
    
    # Add a new 'Category' column based on 'Age' range
    df['Category'] = pd.cut(df['Age'], bins=[0, 18, 65, 100], labels=['Child', 'Adult', 'Senior'])

    return df