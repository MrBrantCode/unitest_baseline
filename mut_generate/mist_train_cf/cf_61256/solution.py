"""
QUESTION:
Write a function `correct_standard_deviation` that calculates the standard deviation of a given list of numbers using the pandas library. The function should handle the case where an empty list is passed to prevent a DivideByZero error.
"""

import pandas as pd

def correct_standard_deviation(numbers):
    if len(numbers) == 0: 
        return None
    
    return pd.Series(numbers).std()