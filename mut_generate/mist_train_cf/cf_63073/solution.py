"""
QUESTION:
Write a function `calCoefficient(data)` that calculates the coefficient of variation of a given list of numbers. The coefficient of variation is the standard deviation divided by the mean. The function should handle exceptions, including division by zero errors and empty input lists. The function should return `None` if the calculation is not possible.
"""

import math
import statistics

def calCoefficient(data):
    if len(data) == 0: 
        return None
    mean = statistics.mean(data)
    
    # Prevent division by zero error.
    if mean == 0:
        return None
    
    std_dev = statistics.stdev(data)
    
    cs = std_dev / mean
    return cs