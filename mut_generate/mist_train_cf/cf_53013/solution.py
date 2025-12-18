"""
QUESTION:
Create a function named `add_reciprocals` that takes a pandas DataFrame as input, appends the reciprocals of each existing column to the DataFrame, and labels them based on the original column names with an 'inv_' prefix. The resulting DataFrame should have the same columns as the original DataFrame plus the reciprocal columns.
"""

def add_reciprocals(df):
    return pd.concat([df, 1 / df.add_prefix('inv_')], axis=1)