"""
QUESTION:
Write a function `nth_smallest(arr, n)` that takes an array of integers `arr` and an integer `n` as input and returns the nth smallest element in the array. The function should work with arrays containing negative numbers and zeroes, and should return an error message if `n` is less than or equal to 0 or greater than the length of the array.
"""

def nth_smallest(arr, n):
    if n <= 0 or n > len(arr):
        return "Invalid position"
    else:
        arr.sort()
        return arr[n-1]