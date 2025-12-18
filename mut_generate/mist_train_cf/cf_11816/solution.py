"""
QUESTION:
Implement a function called `quicksort` that sorts a given list in ascending order using the quicksort algorithm without using any built-in sorting functions or libraries. The function should have an average time complexity of O(n log n) to handle large input sizes efficiently.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)