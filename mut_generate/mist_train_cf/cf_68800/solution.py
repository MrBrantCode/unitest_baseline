"""
QUESTION:
Write a function `find_changed_coins` that takes two pandas DataFrames, `first_df` and `second_df`, each with columns 'country' and 'coin'. The function should return a new DataFrame containing the rows where the country of a coin has changed between the two DataFrames. The returned DataFrame should only include the 'country' and 'coin' columns, with the 'country' values coming from `second_df`.
"""

import pandas as pd

def find_changed_coins(first_df, second_df):
    """
    This function takes two pandas DataFrames, each with columns 'country' and 'coin'.
    It returns a new DataFrame containing the rows where the country of a coin has changed 
    between the two DataFrames. The returned DataFrame only includes the 'country' and 'coin' 
    columns, with the 'country' values coming from second_df.
    """
    merged_df = pd.merge(first_df, second_df, on="coin", suffixes=('_first', '_second'))
    changed_rows = merged_df[merged_df['country_first'] != merged_df['country_second']]
    return changed_rows[['country_second', 'coin']].rename(columns={'country_second': 'country'})