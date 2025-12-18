"""
QUESTION:
Create a function `max_min_median_values` that takes a list of integers as input, calculates the maximum, minimum, and median values of the list, and returns or prints these values. The function should handle lists of any size, and the solution should consider the time and memory complexity of the implementation.
"""

def max_min_median_values(lst):
    max_val = max(lst)
    min_val = min(lst)
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2] + sorted_lst[n//2-1]) / 2
    else:
        median = sorted_lst[n//2]
    return max_val, min_val, median