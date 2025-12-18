"""
QUESTION:
Implement a function `quicksort_descending` that sorts an array of integers in descending order using a variation of the quicksort algorithm without built-in sorting functions or libraries, with a time complexity of O(n log n) and the ability to handle arrays with up to 1,000,000 elements.
"""

def quicksort_descending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort_descending(greater_than_pivot) + [pivot] + quicksort_descending(less_than_pivot)