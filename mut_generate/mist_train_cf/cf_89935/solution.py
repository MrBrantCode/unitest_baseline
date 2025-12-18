"""
QUESTION:
Create a function `quicksort` that sorts an array of integers in descending order without using built-in sorting functions or libraries. The function should be implemented using a variation of the quicksort algorithm, with a time complexity of O(n^2), and be able to handle arrays with up to 10,000,000 elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + middle + quicksort(right)