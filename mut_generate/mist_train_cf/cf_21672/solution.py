"""
QUESTION:
Implement a function `remove_trailing_zeros(num)` that takes a float number as input, removes all trailing zeros after the decimal point, and returns the resulting number as a string. The input number can have at most 10^6 digits after the decimal point, and the solution should have a time complexity of O(n), where n is the number of digits after the decimal point. The solution should not use any built-in functions or libraries to achieve the desired result.
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