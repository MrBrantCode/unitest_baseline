"""
QUESTION:
Write a function named `filter_musicians` that takes a pandas DataFrame `df` as input and returns a new DataFrame containing only the rows where the 'Nationality' column is 'Japan'. The input DataFrame is expected to have columns 'Name', 'Genre', 'Nationality', 'Popularity', and 'Albums Sold'. The function should also include a method to sort the resulting DataFrame based on a specified criteria (e.g., 'Albums Sold' or 'Popularity').
"""

import pandas as pd

def filter_musicians(df, criteria):
    """
    Filter a pandas DataFrame to include only Japanese musicians and sort by a specified criteria.

    Parameters:
    df (pd.DataFrame): The input DataFrame with columns 'Name', 'Genre', 'Nationality', 'Popularity', and 'Albums Sold'.
    criteria (str): The column to sort the resulting DataFrame by.

    Returns:
    pd.DataFrame: A new DataFrame containing only Japanese musicians, sorted by the specified criteria.
    """
    # Filter out non-Japanese musicians
    japanese_musicians = df[df['Nationality'] == 'Japan']
    
    # Sort the resulting DataFrame based on the specified criteria
    sorted_df = japanese_musicians.sort_values(criteria, ascending=False)
    
    return sorted_df