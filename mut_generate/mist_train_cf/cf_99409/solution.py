"""
QUESTION:
Write a function `median` that takes a list of integers as input, sorts it in ascending order, and returns the median value. If the list contains an even number of values, return the average of the two middle values. The function should be able to handle large input lists without memory errors.
"""

def median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]