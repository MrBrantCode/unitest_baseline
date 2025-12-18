"""
QUESTION:
Write a function `find_median(lst)` that takes a list of integers as input and returns the median of the list. The function should handle both cases where the length of the list is odd and even.
"""

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        mid1 = sorted_lst[n//2]
        mid2 = sorted_lst[n//2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_lst[n//2]
    return median