"""
QUESTION:
Write a function named `generate_state_column` that takes a pandas DataFrame `df` with columns 'col1', 'col2', and 'col3' and returns the DataFrame with an additional column 'state'. The 'state' column should have the value of 'col1' if both 'col2' and 'col3' values exceed 50, otherwise, it should have the cumulative value of 'col1', 'col2', and 'col3'.
"""

def generate_state_column(df):
    df['state'] = df.apply(lambda x: x['col1'] if (x['col2'] > 50 and x['col3'] > 50) else x['col1'] + x['col2'] + x['col3'], axis=1)
    return df