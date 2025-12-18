"""
QUESTION:
Create a function named `calculate_miami_rental_medians` that takes a Pandas DataFrame `data` as input, where the DataFrame contains columns 'Rental_Price' and 'Neighborhood'. The function should calculate and return the median rental price for properties in Miami, excluding any properties with a rental price above $10,000 per month, as well as the median rental price for each neighborhood within Miami.
"""

import pandas as pd

def calculate_miami_rental_medians(data: pd.DataFrame) -> tuple:
    """
    Calculate the median rental price for properties in Miami, 
    excluding any properties with a rental price above $10,000 per month, 
    as well as the median rental price for each neighborhood within Miami.

    Args:
        data (pd.DataFrame): A DataFrame containing columns 'Rental_Price' and 'Neighborhood'.

    Returns:
        tuple: A tuple containing the median rental price for Miami and a Series of median rental prices for each neighborhood.
    """

    # Filter out properties with rental price above $10,000 per month
    filtered_data = data[data['Rental_Price'] <= 10000]

    # Calculate the median rental price for Miami
    miami_median = filtered_data['Rental_Price'].median()

    # Calculate the median rental price for each neighborhood within Miami
    neighborhood_median = filtered_data.groupby('Neighborhood')['Rental_Price'].median()

    return miami_median, neighborhood_median