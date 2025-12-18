"""
QUESTION:
Implement a function named `quicksort` that takes a list of numbers as input and returns the list sorted in non-decreasing order. The function should have a time complexity of O(nlogn) and a space complexity of O(logn), and should be able to handle large input sizes (n > 10^6) efficiently, including duplicate and negative numbers.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)