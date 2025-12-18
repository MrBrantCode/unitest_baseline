"""
QUESTION:
Create a function `collect_data_for_linear_regression` to gather the necessary data for predicting the average property value in a city using linear regression. The data should include population density, housing costs, average income, and average property value.
"""

def collect_data_for_linear_regression(city):
    """
    Gather necessary data for predicting average property value in a city using linear regression.
    
    Args:
    city (str): The city for which data is to be collected.
    
    Returns:
    dict: A dictionary containing population density, housing costs, average income, and average property value.
    """
    # Collect data from public sources or primary data collection methods
    # For demonstration purposes, assume we have the following data
    data = {
        'population_density': 1000,  # people per square kilometer
        'housing_costs': 500000,  # average housing cost in the city
        'average_income': 60000,  # average annual income in the city
        'average_property_value': 750000  # average property value in the city
    }
    
    return data