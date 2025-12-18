"""
QUESTION:
Write a function named `abs_list` that takes a list of integers as input and returns a new list containing the absolute values of the input integers. The function should handle lists of any length and contain both positive, negative, and zero values. The implementation should not use any built-in or predefined functions for calculating absolute values.
"""

def abs_list(lst):
    return [n if n >= 0 else -n for n in lst]