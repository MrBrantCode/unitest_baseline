"""
QUESTION:
Write a function called reverse_array that takes an array of integers as input and returns the reversed array. The array may contain both positive and negative integers.
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr