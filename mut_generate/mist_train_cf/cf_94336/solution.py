"""
QUESTION:
Implement the quicksort function to sort an array of integers in ascending order. The function should take an array as input and return the sorted array. It should handle edge cases such as an empty array or an array with only one element. The function should choose the pivot element and partition the array accordingly.
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return entrance(less) + [pivot] + entrance(greater)