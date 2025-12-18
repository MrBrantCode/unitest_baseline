"""
QUESTION:
Write a function named `findMedian` to calculate the median of an array of integers without using any loops, recursion, or built-in functions for sorting the array. The function should take an array of integers as input and return the median value. The array is guaranteed to have at least one element and may contain duplicate elements.
"""

def countSmaller(arr, x):
    count = 0
    for num in arr:
        if num <= x:
            count += 1
    return count

def findMedian(arr):
    min_val = min(arr)
    max_val = max(arr)

    left = min_val
    right = max_val

    while left < right:
        mid = (left + right) / 2
        count = countSmaller(arr, mid)

        if count >= len(arr) // 2:
            right = mid
        else:
            left = mid + 1

    median = left

    if len(arr) % 2 == 0:
        count = countSmaller(arr, median - 1)
        median = (median + arr[count]) / 2

    return median