"""
QUESTION:
Write a function `linear_search_last_occurrence` that takes a sorted list of integers `arr` and a target integer `target` as input. The function should return the index of the last occurrence of the target number in the list. If the target number is not found, return -1. The list can contain up to 10^9 elements and the target number can be any integer within the range of -10^12 to 10^12. The list is guaranteed to be sorted in non-decreasing order.
"""

def linear_search_last_occurrence(arr, target):
    last_occurrence = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            last_occurrence = i
    
    return last_occurrence