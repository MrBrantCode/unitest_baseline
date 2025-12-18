"""
QUESTION:
Write a function `cv(arr)` that calculates the coefficient of variation of a given list of non-negative integers. The coefficient of variation is the ratio of the standard deviation to the mean. Before computation, remove any duplicate elements from the list.
"""

import statistics
def cv(arr):
    arr = list(set(arr))  # remove duplicates
    return statistics.pstdev(arr)/statistics.mean(arr)  # calculate CV