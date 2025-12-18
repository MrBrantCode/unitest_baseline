"""
QUESTION:
Create a function named `linear_search_reverse` that takes two parameters: an array `arr` and a target number `target`. The function should perform a linear search in the array starting from the end and return the index of the last occurrence of the target number. If the target number is not found, the function should return -1. The function should have a time complexity of O(n), where n is the length of the array.
"""

def linear_search_reverse(arr, target):
    index = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            index = i
            break
    return index