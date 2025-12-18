"""
QUESTION:
Implement a function `quicksort(arr)` to sort a large, unordered array of integers efficiently. The function should take an array of integers as input, sort the array in ascending order, and return the sorted array. The function should aim for a time complexity of O(n log n) and should be suitable for a general-purpose sorting algorithm.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)