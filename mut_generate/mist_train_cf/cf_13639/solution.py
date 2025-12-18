"""
QUESTION:
Implement a function called quicksort that takes a list of integers as input and returns a sorted list using the quicksort algorithm. The function should recursively partition the list into sublists based on a chosen pivot element, and the base case is when the length of the list is less than or equal to 1.
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return entrance(less) + [pivot] + entrance(greater)