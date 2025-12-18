"""
QUESTION:
Implement an iterative quicksort algorithm using a stack to sort a given list of integers in ascending order, without using any built-in sorting functions or libraries. The function, named `quicksort`, should take a list `arr` as input and return the sorted list. The implementation should have an average time complexity of O(n log n) and be able to handle large input sizes efficiently.
"""

def quicksort(arr):
    """
    Sorts a list of integers in ascending order using the quicksort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    stack = []
    stack.append((0, len(arr)-1))

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        pivot_index = partition(arr, low, high)
        stack.append((low, pivot_index-1))
        stack.append((pivot_index+1, high))

    return arr

def partition(arr, low, high):
    """
    Partitions the array around a pivot element.

    Args:
        arr (list): A list of integers.
        low (int): The low index of the subarray.
        high (int): The high index of the subarray.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1