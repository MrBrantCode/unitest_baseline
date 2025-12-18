"""
QUESTION:
Write a function named `linear_search` that takes a list of integers and a target integer as input and returns the index of the first occurrence of the target number in the list. If the target number is not found, return -1. The input list can contain up to 10^6 elements, and the target number can be any integer within the range of -10^9 to 10^9.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1