"""
QUESTION:
Write a function `linear_search_last_occurrence(arr, target)` that performs a linear search in a given sorted list of integers `arr` to find the index of the last occurrence of a target number `target`. The function should return the index of the last occurrence if the target number is found, and -1 if it is not found. The list `arr` contains up to 10^9 elements and is guaranteed to be sorted in non-decreasing order. The target number `target` can be any integer within the range of -10^12 to 10^12.
"""

def linear_search_last_occurrence(arr, target):
    n = len(arr)
    last_occurrence = -1
    
    for i in range(n):
        if arr[i] == target:
            last_occurrence = i
    
    return last_occurrence