"""
QUESTION:
Implement a function named `customSort` that sorts an array of integers in ascending order. The input array can contain positive and negative integers and will not be empty. The function should have a time complexity of O(nlogn) and must not use any built-in sorting functions or libraries. It can, however, use additional helper functions if necessary.
"""

def customSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return customSort(less) + [pivot] + customSort(greater)