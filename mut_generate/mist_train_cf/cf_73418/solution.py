"""
QUESTION:
Create a function called `get_min_count_rows` that takes a pandas DataFrame `df` as input, groups it by the columns 'Sp' and 'Mt', and returns a new DataFrame containing all rows where the 'count' value is the minimum within each group.
"""

def get_min_count_rows(df):
    df['rank'] = df.groupby(['Sp','Mt'])['count'].rank(method='min')
    result = df[df['rank'] == 1].copy()
    df.drop('rank', axis=1, inplace=True)
    return result