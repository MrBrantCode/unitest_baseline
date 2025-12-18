"""
QUESTION:
Write a function `calculate_median` that calculates the median of an array of integers. The array may contain duplicate elements and will always have at least one element. The function should not use any built-in functions for sorting the array.
"""

def calculate_median(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    n = length
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median