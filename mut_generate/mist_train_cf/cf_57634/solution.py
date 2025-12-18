"""
QUESTION:
Create a function named `f` that takes a pandas DataFrame `df` as input and returns a list of non-integer values in the 'Field1' column. The function should iterate through each value in the column, check if it is an integer using `isinstance(value, int)`, and append non-integer values to the list.
"""

def f(df):
    """
    Returns a list of non-integer values in the 'Field1' column of a pandas DataFrame.

    Args:
        df (pandas DataFrame): Input DataFrame.

    Returns:
        list: List of non-integer values in the 'Field1' column.
    """
    errors = []
    for value in df['Field1']:
        if not isinstance(value, int):
            errors.append(value)
    return errors