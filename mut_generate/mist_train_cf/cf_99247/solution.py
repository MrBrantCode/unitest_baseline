"""
QUESTION:
Create a function named `max_min_median_values` that takes a list of integers as input and returns or prints the maximum, minimum, and median values of the list. The function should handle both even and odd length lists when calculating the median. The solution should be optimized for time and memory complexity, considering potential large input sizes.
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