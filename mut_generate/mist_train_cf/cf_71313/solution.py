"""
QUESTION:
Implement the `quicksort` function to sort an array of items. The function should recursively divide the array into three subarrays: elements less than a chosen pivot, elements equal to the pivot, and elements greater than the pivot, and return the sorted array. The input array may contain duplicate elements.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)