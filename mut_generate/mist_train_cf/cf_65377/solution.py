"""
QUESTION:
Write a function named `calculate_wind_chill_index` that calculates the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in Celsius. The function should handle edge cases where the temperature is above 10 degrees Celsius or the wind speed is less than 4.8 km/h and return a custom error message for these edge cases.
"""

import math

def calculate_wind_chill_index(velocity, temperature):
    """ Calculate wind chill index """

    if temperature > 10:
        return 'Wind chill index cannot be reliably calculated for temperatures above 10°C'
    if velocity < 4.8:
        return 'Wind chill index cannot be reliably calculated for wind speeds less than 4.8 km/h'

    return round(13.12 + 0.6215*temperature - 11.37*math.pow(velocity, 0.16) + 0.3965*temperature*math.pow(velocity, 0.16))