"""
QUESTION:
Write a function `reverse_array` to reverse the order of elements in a given array of integers. The function should take one argument: an array of integers, and return the reversed array.
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr