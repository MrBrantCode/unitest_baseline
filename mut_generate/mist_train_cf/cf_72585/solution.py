"""
QUESTION:
Write a function `filter_closing_price` that takes a pandas DataFrame `df` and returns a new DataFrame containing only the rows where the value in the 'closing_price' column falls within the range of 99 and 101 (inclusive).
"""

def filter_closing_price(df):
    return df[(df['closing_price'] >= 99) & (df['closing_price'] <= 101)]