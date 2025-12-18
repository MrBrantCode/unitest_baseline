"""
QUESTION:
Write a function `filter_elements` that takes a list of integers `lst` and an integer `arg`, and returns a list of elements from `lst` that are greater than `arg` and divisible by 3.
"""

def filter_elements(lst, arg):
    return [num for num in lst if num > arg and num % 3 == 0]