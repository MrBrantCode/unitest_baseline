"""
QUESTION:
Create a function named `verify_value` that takes three parameters: `value`, `start`, and `end`. The function should return `True` if `value` is a real number and falls within the range defined by `start` and `end` (inclusive), and `False` otherwise. The function should handle potential exceptions where the user might input non-number values for the range or the value being checked without using any built-in Python functions for type checking.
"""

def verify_value(value, start, end):
    try:
        real_number = float(value)
        start_point = float(start)
        end_point = float(end)
    except ValueError:
        return False
    
    if start_point <= real_number <= end_point:
        return True
    else:
        return False