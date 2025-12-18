"""
QUESTION:
Implement a function called `quick_sort` that takes a list of integers as input and returns a new list containing the same integers in sorted order. The function should use the quick sort algorithm to achieve this. The function should not modify the input list and should be able to handle lists of any length, including empty lists.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)