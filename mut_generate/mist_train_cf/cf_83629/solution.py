"""
QUESTION:
Implement the `quicksort` function to sort an array of integers, handling duplicate integers and efficiently managing larger arrays. The function should take an array as input and return the sorted array. The implementation should have an average time complexity of O(n log n).
"""

def quicksort(arr):
    """
    This function takes an array and returns a sorted version of it using quicksort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)