"""
QUESTION:
Write a recursive function `reverse_number` that takes a string `num_str` as input and returns the string with its digits in reverse order. The function should handle negative numbers and leading zeroes without using Python's built-in `reverse()` function or string slicing method.
"""

def reverse_number(num_str, index=None):
    if index is None:
        index = len(num_str)-1
    if index < 0:
        return ""
    if num_str[0] == '-':
        if index == 0:
            return num_str[0]
        else:
            return reverse_number(num_str, index-1) + num_str[index]
    else:
        return num_str[index] + reverse_number(num_str, index-1)