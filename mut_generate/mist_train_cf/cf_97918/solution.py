"""
QUESTION:
Write a function `median(lst)` in Python that calculates the median of a given list of integers `lst`. The function should first sort the list in ascending order, then return the middle value if the list has an odd number of elements, or the average of the two middle values if the list has an even number of elements. The function should be able to handle lists of any size without causing memory errors.
"""

def median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]