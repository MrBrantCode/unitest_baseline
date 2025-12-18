"""
QUESTION:
Write a function `convert_to_decimal` that takes a string of digits `num_str` and an integer `base` as input, and returns the decimal equivalent of the number represented by `num_str` in the given base. The function should support bases from 2 to 10. If the base is outside this range, the function should return an error message.
"""

def convert_to_decimal(num_str, base):
    if 2 <= base <= 10:
        return int(num_str, base)
    else:
        return "Invalid base. Please enter a base between 2 and 10."