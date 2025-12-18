"""
QUESTION:
Create a function called `merge_dataframes` that merges two pandas dataframes based on multiple specific columns with different merge methods. The function should take three parameters: `df1` and `df2` as the two dataframes to be merged, and `merge_info` as a dictionary where the keys are the column names and the values are the merge methods. The function should return a new merged dataframe.
"""

import pandas as pd

def merge_dataframes(df1, df2, merge_info):
    """
    Merge two pandas dataframes based on multiple specific columns with different merge methods.

    Parameters:
    df1 (pd.DataFrame): The first dataframe to be merged.
    df2 (pd.DataFrame): The second dataframe to be merged.
    merge_info (dict): A dictionary where the keys are the column names and the values are the merge methods.

    Returns:
    pd.DataFrame: A new merged dataframe.
    """
    if len(merge_info) != len(set(merge_info.values())):
        # Group the merge methods
        grouped_merge_info = {}
        for column, method in merge_info.items():
            if method not in grouped_merge_info:
                grouped_merge_info[method] = []
            grouped_merge_info[method].append(column)

        # Initialize the merged dataframe with df1
        merged_df = df1

        # Iterate over each merge method and its corresponding columns
        for method, columns in grouped_merge_info.items():
            # Merge the dataframes based on the specified columns and merge method
            merged_df = pd.merge(merged_df, df2, on=columns, how=method)
    else:
        # If all merge methods are the same, merge directly
        merged_df = pd.merge(df1, df2, on=list(merge_info.keys()), how=list(merge_info.values())[0])

    return merged_df