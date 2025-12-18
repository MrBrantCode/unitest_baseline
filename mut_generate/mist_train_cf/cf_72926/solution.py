"""
QUESTION:
Write a function `groupby_average` that takes a Pandas DataFrame as input and returns a new DataFrame. Group the input DataFrame by the 'Product Category' and 'Region' fields, calculate the average price of each 'Product Category' per 'Region', and reset the index.
"""

def groupby_average(df):
    return df.groupby(['Region', 'Product Category'])['Price'].mean().reset_index()