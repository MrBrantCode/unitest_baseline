"""
QUESTION:
Implement a function called `calculate_dividend_growth_rate` that takes a list of dividend values and their corresponding years as input, and returns the annual dividend growth rate. The function should be able to use two methods: a simple method that calculates the growth rate based on the first and last dividend values, and a more complex method that uses an exponential function with a least squares approach, giving more weight to recent dividends.
"""

import numpy as np

def calculate_dividend_growth_rate(dividends, years):
    """
    Calculate the annual dividend growth rate.

    Args:
    dividends (list): A list of dividend values.
    years (list): A list of years corresponding to the dividend values.

    Returns:
    tuple: A tuple containing the simple growth rate and the complex growth rate using an exponential function with a least squares approach.
    """
    
    # Calculate the simple growth rate
    simple_growth_rate = (dividends[-1] / dividends[0]) ** (1 / (years[-1] - years[0])) - 1

    # Calculate the complex growth rate using an exponential function with a least squares approach
    years_array = np.array(years)
    dividends_array = np.array(dividends)
    coefficients = np.polyfit(years_array, np.log(dividends_array), 1)
    complex_growth_rate = np.exp(coefficients[0]) - 1

    return simple_growth_rate, complex_growth_rate