"""
QUESTION:
Write a function `calculate_vehicle_frequency_and_mean_price` that takes a pandas DataFrame, a column name for vehicle type, a column name for color, and a column name for price. Calculate the frequency of each unique vehicle type and then group the DataFrame by color and vehicle type, calculating the mean price for each unique vehicle type under each color.
"""

import pandas as pd

def calculate_vehicle_frequency_and_mean_price(df, vehicle_column, color_column, price_column):
    """
    Calculate the frequency of each unique vehicle type and then group the DataFrame by color and vehicle type, 
    calculating the mean price for each unique vehicle type under each color.

    Args:
        df (pd.DataFrame): Input DataFrame.
        vehicle_column (str): Name of the column for vehicle type.
        color_column (str): Name of the column for color.
        price_column (str): Name of the column for price.

    Returns:
        tuple: A tuple containing the frequency of each vehicle type and the mean price for each vehicle type under each color.
    """

    # Find the frequency of each value under 'vehicle'
    vehicle_counts = df[vehicle_column].value_counts()

    # Group by 'color' and 'vehicle', and calculate mean price
    grouped = df.groupby([color_column, vehicle_column])[price_column].mean().reset_index()

    return vehicle_counts, grouped