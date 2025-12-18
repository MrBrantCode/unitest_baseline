"""
QUESTION:
Implement a function called `quick_sort` that takes a list of integers as input and returns the sorted list in ascending order. Use the QuickSort algorithm, which employs a divide-and-conquer approach by partitioning the list around a pivot element and recursively sorting the sub-lists. Ensure that the function works correctly for lists of varying lengths, including empty lists and lists with duplicate elements.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)