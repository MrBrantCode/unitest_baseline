"""
QUESTION:
Create a function `alternate_page_data` that takes a dataset and a list of column names as input and returns two separate datasets, one for odd pages and one for even pages. The function should not use any GUI or reporting tools, and should not require a specific database management system.
"""

import pandas as pd

def alternate_page_data(dataset, column_names):
    """
    This function takes a dataset and a list of column names as input, 
    and returns two separate datasets, one for odd pages and one for even pages.

    Parameters:
    dataset (pandas DataFrame): The input dataset.
    column_names (list): A list of column names.

    Returns:
    tuple: Two separate DataFrames, one for odd pages and one for even pages.
    """
    
    # Filter the dataset to include only the specified columns
    filtered_dataset = dataset[column_names]
    
    # Split the dataset into two separate DataFrames, one for odd pages and one for even pages
    odd_pages = filtered_dataset[1::2]
    even_pages = filtered_dataset[::2]
    
    return odd_pages, even_pages