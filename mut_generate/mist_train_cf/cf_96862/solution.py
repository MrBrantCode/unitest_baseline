"""
QUESTION:
Create a function named `quicksort_descending` to sort an array of integers in descending order using a variation of the quicksort algorithm, without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and be able to handle arrays with up to 1,000,000 elements.
"""

def quicksort_descending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort_descending(greater_than_pivot) + [pivot] + quicksort_descending(less_than_pivot)