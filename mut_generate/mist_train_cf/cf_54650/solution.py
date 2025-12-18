"""
QUESTION:
Create a function `remove_trailing_zeros(num)` that takes a float number as input, removes trailing zeros after the decimal point, and returns the result. The function should handle cases where the input may be an integer, a float with trailing zeros, or a float without trailing zeros, and return the result in its original type if no trailing zeros are present.
"""

def remove_trailing_zeros(num):
    str_num = ('%f' % num).rstrip('0').rstrip('.')
    return str_num if '.' in str_num else int(str_num)