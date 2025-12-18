"""
QUESTION:
Write a function `group_employees_by_birth_year_and_department` that takes a Pandas DataFrame as input, where the DataFrame has columns 'department' and 'birth_date' in string format ('yyyy-mm-dd'). The function should return a grouped DataFrame with employees grouped by their birth year and department. The birth year should be extracted from the 'birth_date' column.
"""

import pandas as pd

def group_employees_by_birth_year_and_department(df):
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['birth_year'] = df['birth_date'].dt.year
    return df.groupby(['birth_year', 'department'])['name'].apply(list)