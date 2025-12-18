"""
QUESTION:
Write a function named `median` that takes a list of integers as input. The function should sort the input list in ascending order and return the median value. If the list has an even number of values, the function should return the average of the two middle values. The function must be able to handle large input lists efficiently.
"""

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]