"""
QUESTION:
Write a function called `remove_trailing_zeros` that takes a floating point number as input and returns its string representation with all trailing zeros after the decimal point removed. The input number can have up to 10^6 digits before and after the decimal point. The solution should have a time complexity of O(n), where n is the number of digits after the decimal point, and should not use any built-in functions or libraries to achieve the desired result.
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