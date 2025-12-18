"""
QUESTION:
Create a function called `median` that takes a list of numbers as input and returns the median value. The list may have an odd or even number of elements. The function should handle both cases correctly, returning the middle value for odd-length lists and the average of the two middle values for even-length lists.
"""

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

import statistics

def median(lst):
    return statistics.median(lst)