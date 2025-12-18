"""
QUESTION:
Implement a function called `calculate_median` that calculates the median of a given array of integers, which can be of any length, contain duplicates, and have both positive and negative numbers. The function should have a time complexity of O(nlogn), where n is the length of the input array.
"""

def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        median = (sorted_arr[mid1] + sorted_arr[mid2]) / 2
    else:
        mid = n // 2
        median = sorted_arr[mid]
    return median