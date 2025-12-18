"""
QUESTION:
Write a function called `find_consecutive_pairs` that takes an array and an integer value as input. The function should return the indices of the first occurrence of two consecutive elements in the array that are equal to the given value. If no such pair exists, the function should return None. The input array will have at least three elements and the given value will be an integer.
"""

def find_consecutive_pairs(arr, value):
    for i in range(len(arr)-1):
        if arr[i] == value and arr[i+1] == value:
            return [i, i+1]
    return None