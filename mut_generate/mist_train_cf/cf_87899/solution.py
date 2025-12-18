"""
QUESTION:
Write a function called `calculate_median` that calculates the median of an array with an odd number of elements without using built-in functions, loops, recursion, or additional data structures. The input array will not be modified and the function should use constant extra space, achieving a time complexity of O(n) or less.
"""

def calculate_median(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    median = arr[middle_index]
    return median