"""
QUESTION:
Write a function `calculateMedian` that takes an array of integers as input, sorts the array in ascending order, and returns the median value. If the length of the array is even, the median is the average of the two middle numbers. If the length of the array is odd, the median is the middle number. The array can contain any number of integers.
"""

def calculateMedian(arr):
    n = len(arr)
    arr.sort()
 
    if n % 2 == 0:
        median1 = arr[n//2]
        median2 = arr[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = arr[n // 2]
 
    return median