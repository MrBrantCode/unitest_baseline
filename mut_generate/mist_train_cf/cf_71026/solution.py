"""
QUESTION:
Create a function `get_max_count_rows` that takes a pandas DataFrame as input, groups it by the columns 'Sp' and 'Mt', and returns the rows where the 'count' value is maximum within each group.
"""

def get_max_count_rows(df):
    df['max_count'] = df.groupby(['Sp', 'Mt'])['count'].transform('max')
    return df[df['count'] == df['max_count']].drop(columns=['max_count'])