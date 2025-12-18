"""
QUESTION:
Create a function called `filter_rows_by_city` that takes a pandas DataFrame and a dictionary where keys are city names and values are the corresponding number of rows to keep. The function should return a new DataFrame ordered by city, keeping the specified number of rows for each city. The rows to keep should be the top rows based on their original order in the input DataFrame.
"""

import pandas as pd

def filter_rows_by_city(df, city_rows):
    """
    Filter rows in a DataFrame by city, keeping a specified number of rows for each city.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    city_rows (dict): A dictionary where keys are city names and values are the corresponding number of rows to keep.

    Returns:
    pd.DataFrame: A new DataFrame ordered by city, keeping the specified number of rows for each city.
    """
    # Initialize an empty list to store the filtered DataFrames
    filtered_dfs = []

    # Iterate over each city and the corresponding number of rows to keep
    for city, num_rows in city_rows.items():
        # Filter the DataFrame for the current city and keep the specified number of rows
        df_city = df[df['city'] == city].head(num_rows)
        
        # Add the filtered DataFrame to the list
        filtered_dfs.append(df_city)

    # Concatenate the filtered DataFrames
    df_final = pd.concat(filtered_dfs)

    return df_final