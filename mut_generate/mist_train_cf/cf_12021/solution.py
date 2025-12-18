"""
QUESTION:
Create a function named quick_sort_descending that sorts a list of integers in descending order using the Quick Sort algorithm. The function should take a list of integers as input and return the sorted list. The Quick Sort algorithm should select a pivot element from the list, partition the list into two sublists, and recursively apply the same process to each sublist until the entire list is sorted.
"""

def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x < pivot]
        greater_than_pivot = [x for x in arr[1:] if x >= pivot]
        return quick_sort_descending(greater_than_pivot) + [pivot] + quick_sort_descending(less_than_pivot)