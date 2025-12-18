"""
QUESTION:
Write a function `sort_data` that takes a pandas DataFrame and a column name as input and returns the DataFrame sorted by the specified column. The function should have an optional `ascending` parameter with a default value of `True` to specify the sorting order. Include error handling to manage potential issues during execution. Assume the DataFrame has already been cleaned and preprocessed to handle missing values.
"""

def sort_data(df, column, ascending=True):
    """
    Sorts a pandas DataFrame by a specified column.

    Args:
    - df (pd.DataFrame): Input DataFrame.
    - column (str): Column name to sort by.
    - ascending (bool, optional): Sorting order. Defaults to True.

    Returns:
    - pd.DataFrame: Sorted DataFrame.

    Raises:
    - Exception: If an error occurs during sorting.
    """
    try:
        sorted_df = df.sort_values(by=column, ascending=ascending)
        return sorted_df
    except Exception as e:
        print("There was an error: ", e)