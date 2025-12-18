"""
QUESTION:
Implement a `quick_sort` function that takes an array of alphanumeric strings as input and returns the array sorted in ascending lexicographical order, with uppercase letters preceding lowercase letters and special characters arranged according to their ASCII values. The function should be efficient enough to handle large datasets.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        greater = [element for element in arr[1:] if element > pivot]
        lesser = [element for element in arr[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)