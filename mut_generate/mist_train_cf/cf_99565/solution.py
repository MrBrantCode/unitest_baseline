"""
QUESTION:
Implement a function called `selection_sort` that sorts an array of numbers in ascending order. The function should also be modifiable to sort the array in descending order. The array should be sorted in-place, without using any additional data structures that scale with input size. Write two versions of the function: `selection_sort` for ascending order and `selection_sort_descending` for descending order.
"""

def selection_sort(arr):
    """
    Sorts an array of numbers in ascending order.

    Args:
        arr (list): A list of numbers.

    Returns:
        list: The sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_descending(arr):
    """
    Sorts an array of numbers in descending order.

    Args:
        arr (list): A list of numbers.

    Returns:
        list: The sorted list in descending order.
    """
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr