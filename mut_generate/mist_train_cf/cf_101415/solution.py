"""
QUESTION:
Write a function called `group_employees` that takes a Pandas DataFrame as input, with columns 'department' and 'birth_date' (in 'yyyy-mm-dd' string format), and returns a grouped DataFrame or Series with employees grouped by their birth year and department. The function should handle the conversion of 'birth_date' from string to datetime format and extract the birth year.
"""

import pandas as pd

def group_employees(df):
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['birth_year'] = df['birth_date'].dt.year
    return df.groupby(['birth_year', 'department'])['name'].apply(list)