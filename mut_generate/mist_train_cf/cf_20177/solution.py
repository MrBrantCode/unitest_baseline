"""
QUESTION:
Define a function `filter_and_sort_countries` that takes a pandas DataFrame `df` and a country name `country_name` as input. The DataFrame should contain the columns 'Country', 'Population (in millions)', and 'GDP (in billions)'. The function should filter the DataFrame to exclude the input country and include only countries with a population greater than 10 million, then sort the remaining records in descending order based on 'GDP (in billions)'.
"""

import pandas as pd

def filter_and_sort_countries(df, country_name):
    """
    This function filters a pandas DataFrame to exclude the input country and 
    include only countries with a population greater than 10 million, then 
    sorts the remaining records in descending order based on 'GDP (in billions)'.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing 'Country', 'Population (in millions)', 
                       and 'GDP (in billions)' columns.
    country_name (str): The name of the country to be excluded.

    Returns:
    pd.DataFrame: The filtered and sorted DataFrame.
    """
    # Filter the records based on the input country name and population > 10 million
    filtered_df = df[(df['Country'] != country_name) & (df['Population (in millions)'] > 10)]

    # Sort the remaining records based on GDP in descending order
    sorted_df = filtered_df.sort_values('GDP (in billions)', ascending=False)

    return sorted_df