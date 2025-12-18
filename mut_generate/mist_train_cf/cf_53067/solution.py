"""
QUESTION:
Write a function `sample_function` that takes an integer `value` as input. The function should return the result of multiplying `value` by 2 if it's greater than 20, and by 4 otherwise. The return value should be consistent in type.
"""

def sample_function(value):
    if value > 20:
        result = value * 2
    else:
        result = value * 4
    return result