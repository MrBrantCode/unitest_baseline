"""
QUESTION:
Write a function `count_values` that takes a pandas DataFrame `df` and two column names `col1` and `col2` as input. The function should return a dictionary where the keys are the unique entries of `col1` and the values are dictionaries. These sub-dictionaries should contain each unique value from `col2` as keys and the count of these values as values. The function should not take any additional arguments.
"""

def count_values(df, col1, col2):
    """
    This function takes a pandas DataFrame `df` and two column names `col1` and `col2` as input.
    It returns a dictionary where the keys are the unique entries of `col1` and the values are dictionaries.
    These sub-dictionaries contain each unique value from `col2` as keys and the count of these values as values.

    Parameters:
    df (DataFrame): Input DataFrame.
    col1 (str): First column name.
    col2 (str): Second column name.

    Returns:
    dict: Dictionary with counts of values.
    """
    dict_count = {}
    for value1 in df[col1].unique():
        sub_dict = {}
        for value2 in df[df[col1] == value1][col2].unique():
            sub_dict[value2] = df[(df[col1] == value1) & (df[col2] == value2)].shape[0]
        dict_count[value1] = sub_dict
    return dict_count