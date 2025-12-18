"""
QUESTION:
Write a function named `remove_trailing_zeros` that takes a float number as input and returns a string representation of the number with all trailing zeros after the decimal point removed. The input number can have at most 10^6 digits after the decimal point and at most 10^6 digits before the decimal point. The function should have a time complexity of O(n), where n is the number of digits after the decimal point, and should not use any built-in functions or libraries to achieve the desired result.
"""

def remove_trailing_zeros(num):
    num_str = str(num)
    decimal_pos = num_str.find('.')
    i = len(num_str) - 1

    while i > decimal_pos and num_str[i] == '0':
        i -= 1

    result = num_str[:i+1]

    if result.endswith('.'):
        result = result[:-1]

    return result