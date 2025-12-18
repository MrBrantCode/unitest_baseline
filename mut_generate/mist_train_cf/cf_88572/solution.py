"""
QUESTION:
Implement a function named `quicksort` that sorts a list of numbers in non-decreasing order, handling duplicates and negative numbers, with a time complexity of O(nlogn) and a space complexity of O(logn). The function should take a list `arr` as input and return the sorted list.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)