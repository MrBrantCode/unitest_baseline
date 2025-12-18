"""
QUESTION:
Implement a function `calculate_median` that takes a list of integers as input and returns the median value. The input list can contain both positive and negative integers, can have an odd or even length, and can contain duplicate elements. The implementation must have a time complexity of O(nlogn), where n is the length of the input list.
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