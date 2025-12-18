"""
QUESTION:
Implement the `customSort` function to sort an array of integers in ascending order with a time complexity of O(nlogn) without using any built-in sorting functions or libraries. The input array can contain positive and negative integers and will not be empty.
"""

def customSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return customSort(less) + [pivot] + customSort(greater)