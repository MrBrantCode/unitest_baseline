"""
QUESTION:
Write a function `find_median` that calculates the median of an array of integers. The array may contain duplicate values. The function should take a list of integers as input and return the median value as a number. The median is the middle value in a sorted list. If the list has an even number of elements, the median is the average of the two middle values.
"""

def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2] + sorted_arr[n//2 - 1]) / 2
    else:
        return sorted_arr[n//2]