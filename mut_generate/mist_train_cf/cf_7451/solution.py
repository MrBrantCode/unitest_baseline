"""
QUESTION:
Implement a function named `quicksort` to sort a given array of integers in descending order. The function should not use any built-in sorting functions or libraries and should be based on the quicksort algorithm. The function should have a time complexity of O(n log n) on average and be able to handle arrays with up to 10,000,000 elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + middle + quicksort(right)