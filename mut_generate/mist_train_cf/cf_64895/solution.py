"""
QUESTION:
Given a pandas DataFrame and a value in column A, write a function `get_corresponding_value` to find the corresponding value in column B. The function should take two parameters: the DataFrame `df` and the value `value_in_A`. The function should return the corresponding value in column B. Assume that there may be multiple rows with the same value in column A, and if so, return all corresponding values in column B.
"""

def get_corresponding_value(df, value_in_A):
    """
    This function takes a pandas DataFrame and a value in column A, 
    then returns the corresponding value(s) in column B.

    Parameters:
    df (pandas DataFrame): The DataFrame to search in.
    value_in_A: The value to search for in column A.

    Returns:
    The corresponding value(s) in column B.
    """
    return df.loc[df['Column A'] == value_in_A, 'Column B'].values