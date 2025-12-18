"""
QUESTION:
Define a function `calculate_median(arr)` that calculates the median of a given array of numbers. The array will always have an odd number of elements. You are not allowed to use any built-in functions or libraries to find the median, loops, recursion, or additional data structures, and you cannot modify the input array. The implementation should only use constant extra space and have a time complexity of O(n) or better.
"""

def calculate_median(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    return arr[middle_index]