"""
QUESTION:
Remove trailing zeros from a given floating point number and return the result as a string. The input number can have at most 10^6 digits before and after the decimal point. The function should achieve a time complexity of O(n), where n is the number of digits after the decimal point, and should not use any built-in functions or libraries beyond the input and output string variables. The function should be named 'remove_trailing_zeros'.
"""

def remove_trailing_zeros(num):
    num_str = str(num)
    decimal_index = num_str.index('.')
    i = len(num_str) - 1
    while i > decimal_index:
        if num_str[i] == '0':
            num_str = num_str[:i]
        else:
            break
        i -= 1
    if num_str[-1] == '.':
        num_str = num_str[:-1]
    return num_str