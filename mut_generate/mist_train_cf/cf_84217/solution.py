"""
QUESTION:
Write a function `get_max_count_rows` that takes a pandas DataFrame `df` as input. The function should return a new DataFrame containing the rows with the maximum 'count' for each group of 'Sp' and 'Mt' from the original DataFrame. The input DataFrame has columns 'Sp', 'Mt', 'Value', and 'count'. The function should not take any additional arguments.
"""

def get_max_count_rows(df):
    """
    Returns a new DataFrame containing the rows with the maximum 'count' for each group of 'Sp' and 'Mt' from the original DataFrame.

    Parameters:
    df (pandas DataFrame): The input DataFrame with columns 'Sp', 'Mt', 'Value', and 'count'.

    Returns:
    pandas DataFrame: A new DataFrame containing the rows with the maximum 'count' for each group of 'Sp' and 'Mt'.
    """
    return df.loc[df.groupby(['Sp','Mt'])['count'].idxmax()]