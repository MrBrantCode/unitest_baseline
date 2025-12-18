"""
QUESTION:
Write a function `filter_products` that takes a pandas DataFrame `df` with columns "product_name", "store_location", "country", and "price" as input, and returns a new DataFrame containing only the rows where the "price" is greater than 100 and the "country" starts with the letter "A". The resulting DataFrame should only include the columns "product_name", "store_location", and "country".
"""

import pandas as pd

def filter_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters a DataFrame of products to include only rows where the price is greater than 100 
    and the country starts with the letter 'A'.

    Args:
    df (pd.DataFrame): A DataFrame with columns 'product_name', 'store_location', 'country', and 'price'.

    Returns:
    pd.DataFrame: A new DataFrame containing the filtered rows and only the columns 'product_name', 'store_location', and 'country'.
    """
    
    # Filter the DataFrame to include only rows where the price is greater than 100 and the country starts with 'A'
    filtered_df = df[(df['price'] > 100) & (df['country'].str.startswith('A'))]
    
    # Select only the required columns
    result_df = filtered_df[['product_name', 'store_location', 'country']]
    
    return result_df