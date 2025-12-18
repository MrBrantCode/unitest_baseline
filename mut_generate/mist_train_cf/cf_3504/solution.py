"""
QUESTION:
Implement a function `quicksort(arr)` that takes a list of integers as input and returns a sorted list. The implementation should handle duplicate values efficiently and have an average-case time complexity of O(n log n) and an average-case space complexity of O(log n).
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)