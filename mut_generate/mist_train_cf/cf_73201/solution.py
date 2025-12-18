"""
QUESTION:
Write a function `calculate_absolute_value` that takes a complex number as input from the user, calculates its absolute value, and returns the result. The input complex number should be in the format 'a+bj' where 'a' and 'b' are integers or floats.
"""

import cmath

def calculate_absolute_value(complex_num):
    return cmath.polar(complex(complex_num))[0]