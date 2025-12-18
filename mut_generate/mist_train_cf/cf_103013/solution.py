"""
QUESTION:
Create a function called `linear_search_backwards` that performs a linear search in an array from the end towards the start. The function should take an array `arr` and a target number `target` as input and return the index of the first occurrence of the target number in the array. If the target number is not found, the function should return -1.
"""

def linear_search_backwards(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1