"""
QUESTION:
Implement a function `sort_array` that sorts an array of integers using the Quicksort algorithm. The function should return the sorted array and have a time complexity of O(n log n).
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_array(left) + middle + sort_array(right)