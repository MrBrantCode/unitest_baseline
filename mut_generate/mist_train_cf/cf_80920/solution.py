"""
QUESTION:
Create a function `filter_with_logical_or` that takes a Pandas DataFrame `df` as input and filters its rows based on the condition where column 'A' is greater than 2 or column 'B' equals 'a'. The function should return the filtered DataFrame. Use the logical OR operator "|" for combining the conditions.
"""

def filter_with_logical_or(df):
    condition1 = df['A'] > 2  # This filters out rows where 'A' is greater than 2
    condition2 = df['B'] == 'a'  # This filters out rows where 'B' equals 'a'

    # Now, combine these conditions using the "|" operator
    filtered_df = df[condition1 | condition2]

    return filtered_df