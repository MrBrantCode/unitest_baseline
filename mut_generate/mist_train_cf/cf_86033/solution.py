"""
QUESTION:
Create a function named `calculate_heat_index` that calculates the heat index, rounded to the nearest whole number, given multiple sets of temperature (in Fahrenheit) and relative humidity (in percentage) as input. The function should take a list of tuples, where each tuple contains temperature and humidity, and return a list of results. The function should handle exceptional scenarios where the temperature is below 80 degrees Fahrenheit or the relative humidity is below 40% by returning a custom error message for these cases.
"""

import numpy as np

def calculate_heat_index(weather_conditions):
    heat_index_list = []
    for temp, humidity in weather_conditions:
        if temp < 80 or humidity < 40:
            heat_index_list.append("Error: Temperature and humidity conditions out of range.")
            continue
        heat_index = -42.379 + 2.04901523*temp + 10.14333127*humidity - .22475541*temp*humidity - 6.83783e-3*temp**2\
            -5.481717e-2*humidity**2 + 1.22874e-3*temp**2*humidity + 8.5282e-4*temp*humidity**2 - 1.99e-6*temp**2*humidity**2
        heat_index_list.append(np.around(heat_index))
    return heat_index_list