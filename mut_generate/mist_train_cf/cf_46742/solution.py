"""
QUESTION:
Write a function called `find_median` that takes an array of floating numbers as input and returns the median value. The function should handle both even and odd length arrays, and it should return `None` if the input array is empty.
"""

def find_median(arr):
    if not arr:
        return None

    arr.sort()

    n = len(arr)

    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2

    else:
        return arr[n//2]