"""
QUESTION:
Implement a function called `linear_search_backwards` that takes an array and a target number as input and returns the index of the last occurrence of the target number in the array. The search should start from the end of the array and iterate backwards. If the target number is not found, the function should return -1.
"""

def linear_search_backwards(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1