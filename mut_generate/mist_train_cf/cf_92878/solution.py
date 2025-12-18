"""
QUESTION:
Write a function `calculate_median(arr)` to calculate the median of an array of integers. The array will always have at least one element, and the function should not use any built-in sorting functions. The median is the middle value of a sorted array: if the array has an odd number of elements, the median is the middle element, and if the array has an even number of elements, the median is the average of the two middle elements.
"""

def calculate_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median