"""
QUESTION:
Write a function `find_median(arr)` that calculates the median of a sorted array. The array may contain duplicate elements, and the function should run in less than log(n) time. The function should return a single median value if the array has an odd number of elements and the average of the two middle values if the array has an even number of elements.
"""

def find_median(arr):
    length = len(arr)
    middle = length // 2

    if length % 2 == 1:
        return arr[middle]
    else:
        return (arr[middle - 1] + arr[middle]) / 2