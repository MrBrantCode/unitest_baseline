"""
QUESTION:
Implement a function named `quicksort_descending` that takes an array of integers as input and returns a new array with the elements sorted in descending order using the quicksort algorithm. The function should be recursive and handle arrays of any length.
"""

def quicksort_descending(arr):
    """
    Sorts an array of integers in descending order using the quicksort algorithm.

    Args:
    arr (list): The input array of integers.

    Returns:
    list: A new array with the elements sorted in descending order.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less_than_pivot = []
    greater_than_pivot = []
    for i in range(len(arr)-1):
        if arr[i] <= pivot:
            less_than_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])
    sorted_less = quicksort_descending(less_than_pivot)
    sorted_greater = quicksort_descending(greater_than_pivot)
    return sorted_greater + [pivot] + sorted_less