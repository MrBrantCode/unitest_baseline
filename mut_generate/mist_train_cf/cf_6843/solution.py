"""
QUESTION:
Implement the `modified_quicksort` function that takes a list of integers and a positive integer `k` as input. The function should sort the list using a modified quicksort algorithm, where the pivot is chosen as the median of the first, middle, and last element. If a sublist has at most `k` elements, use insertion sort instead of recursion.
"""

def modified_quicksort(arr, k):
    """
    Sorts the input list using a modified quicksort algorithm.
    
    The pivot is chosen as the median of the first, middle, and last element.
    If a sublist has at most k elements, use insertion sort instead of recursion.

    Args:
        arr (list): A list of integers.
        k (int): A positive integer.

    Returns:
        list: The sorted list.
    """

    if len(arr) <= k:
        # Use insertion sort for small sublists
        return insertion_sort(arr)
    else:
        # Choose the pivot as the median of the first, middle, and last element
        pivot = sorted([arr[0], arr[len(arr) // 2], arr[-1]])[1]
        
        # Partition the list around the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        # Recursively sort the left and right sublists
        return modified_quicksort(left, k) + middle + modified_quicksort(right, k)


def insertion_sort(arr):
    """
    Sorts the input list using insertion sort.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr