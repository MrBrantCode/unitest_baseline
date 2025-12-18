"""
QUESTION:
Write a Python function named `find_extremes` that takes a list of integers as input and returns a tuple containing the maximum value, minimum value, second maximum value, and second minimum value. Assume the input list will always have at least four distinct integers.
"""

def find_extremes(lst):
    max_val = max(lst)
    min_val = min(lst)
    second_max = max(i for i in lst if i != max_val)
    second_min = min(i for i in lst if i != min_val)
    return (max_val, min_val, second_max, second_min)