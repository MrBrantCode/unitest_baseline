"""
QUESTION:
Find the outlier in a given array of integers. The outlier is the number that is furthest from the average of the array. Write a function `find_outlier(arr)` that takes an array of integers as input and returns the outlier value.
"""

def find_outlier(arr):
    avg = sum(arr) / len(arr)
    max_dist = max(abs(x - avg) for x in arr)
    outlier = next(x for x in arr if abs(x - avg) == max_dist)
    return outlier