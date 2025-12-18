"""
QUESTION:
Create a function called `bin_dataframe` that takes a pandas DataFrame as input and returns a new DataFrame where the input DataFrame is grouped into bins of 3 rows each, and the values within each bin are summed. The resulting DataFrame should have a single column 'col1'.
"""

def bin_dataframe(df):
    return df.groupby(df.index // 3).sum()['col1']