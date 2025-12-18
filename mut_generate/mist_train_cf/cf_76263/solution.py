"""
QUESTION:
Write a function `get_mobile_numbers` that takes a pandas DataFrame `df` as input, where the DataFrame contains columns 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5', and 'MobileNo'. The function should return a list of 'MobileNo' values where any of the 'Tag' columns contain a specified tag value.

The function should have the following signature: `def get_mobile_numbers(df, tag_value):`. The function should return a list of strings representing the 'MobileNo' values.
"""

def get_mobile_numbers(df, tag_value):
    return df[df.isin([tag_value]).any(axis=1)]['MobileNo'].values.tolist()