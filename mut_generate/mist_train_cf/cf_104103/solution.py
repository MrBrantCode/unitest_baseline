"""
QUESTION:
Write a recursive function `recursive_sort` that takes an array of integers as input and returns the sorted array. The array may contain both positive and negative integers. The function should not use any built-in sorting functions or libraries. The function should return the array in ascending order.
"""

def recursive_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return recursive_sort(less) + [pivot] + recursive_sort(greater)