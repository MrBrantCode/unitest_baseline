"""
QUESTION:
Implement a recursive quicksort function named `quicksort` that takes a list of integers as input and returns the sorted list without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)