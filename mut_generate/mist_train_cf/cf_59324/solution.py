"""
QUESTION:
Implement a function named `findMin(arr, n)` that takes an array `arr` and its size `n` as input, and returns the smallest integer in the array along with its position. The function must be recursive and should not use any pre-existing or library functions.
"""

def findMin(arr, n):
    if n == 1: 
        return arr[0], 0
    else: 
        smallest_num, smallest_index = findMin(arr, n-1) 
        if arr[n-1] < smallest_num: 
            return arr[n-1], n-1
        else: 
            return smallest_num, smallest_index