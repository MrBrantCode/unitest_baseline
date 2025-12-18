"""
QUESTION:
Implement a function named `get_emp_stats` that takes a pandas DataFrame `df` as input and returns a new DataFrame containing distinct employee names and their respective counts. The returned DataFrame should be sorted in descending order by the count of each name's appearance. In the case of a tie, the names should be sorted alphabetically in ascending order. The function should be able to handle large data sets efficiently and the employee names are assumed to be in a column named 'name' in the input DataFrame.
"""

import pandas as pd

def get_emp_stats(df):
    counts = df['name'].value_counts()
    result_df = pd.DataFrame({'name':counts.index, 'count':counts.values})
    result_df.sort_values(by=['count','name'],ascending=[False,True],inplace=True)
    result_df.reset_index(drop=True, inplace=True)
    return result_df