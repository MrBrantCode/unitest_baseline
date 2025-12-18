"""
QUESTION:
Write a function `assign_value` that takes an input of any type (including nested lists and dictionaries) and returns the input with the following transformations: 
- assign the value 0 to empty strings, NaN, and negative numbers
- replace any positive even numbers with the value 1
- leave all other values unchanged, including None and non-integer numbers.
"""

import math

def assign_value(lst):
    if isinstance(lst, list):  
        return [assign_value(item) for item in lst]  
    elif isinstance(lst, dict):  
        return {key: assign_value(value) for key, value in lst.items()}  
    elif isinstance(lst, str) and lst == '':  
        return 0
    elif isinstance(lst, float) and math.isnan(lst):  
        return 0
    elif isinstance(lst, int) and lst < 0:  
        return 0
    elif isinstance(lst, int) and lst > 0 and lst % 2 == 0:  
        return 1
    else:
        return lst 