"""
QUESTION:
Write a function called `find_outlier_temperatures` that takes a list of temperature values and returns the average temperature, standard deviation, and a list of temperatures that are more than two standard deviations above or below the average temperature.
"""

import statistics

def find_outlier_temperatures(temperatures):
    average_temp = statistics.mean(temperatures)
    standard_deviation = statistics.stdev(temperatures)
    outliers = [temp for temp in temperatures if temp > average_temp + (2 * standard_deviation) or temp < average_temp - (2 * standard_deviation)]
    return average_temp, standard_deviation, outliers