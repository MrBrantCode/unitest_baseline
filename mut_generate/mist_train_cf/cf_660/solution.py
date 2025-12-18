"""
QUESTION:
Implement a recursive function `quicksort(arr)` in Python that sorts a given array of integers in ascending order. The array may contain both positive and negative integers. The implementation should not use any built-in sorting functions or libraries. The function should have a time complexity of O(n^2) and a space complexity of O(log n), where n is the size of the array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)