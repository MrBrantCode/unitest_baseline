"""
QUESTION:
Create a function named `linear_search_backwards` that performs a linear search in an array, starting from the end and iterating backwards. The function should take two parameters: the input array `arr` and the target number `target`. It should return the index of the first occurrence of the target number in the array; if the target number is not found, it should return -1.
"""

def linear_search_backwards(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1