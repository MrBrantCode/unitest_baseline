"""
QUESTION:
Create a function named `linear_search_backwards` that takes an array `arr` and a target number `target` as parameters. The function should perform a linear search for the target number in the array starting from the end and moving backwards. If the target number is found, return its last occurrence index. If not found, return -1.
"""

def linear_search_backwards(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1