"""
QUESTION:
Create a function `get_age_status` that takes a pandas DataFrame with 'Age' column as input. The function should remove rows with negative or missing values in the 'Age' column and then update the 'Age_Status' column based on the following age ranges: 
- Age between 0 and 17: Child
- Age between 18 and 59: Adult
- Age >= 60: Senior
Return the updated DataFrame.
"""

import pandas as pd 

def get_age_status(df):
  # Step 1: Remove rows with negative & missing values
  df = df[(df['Age'].ge(0)) & (df['Age'].notna())]

  # Step 2: Update the 'Age_Status' 
  df['Age_Status'] = df['Age'].apply(lambda age: 'Child' if age < 18 else 'Adult' if age < 60 else 'Senior')
  return df