"""
QUESTION:
Create a function named `binary_search` that takes in three parameters: `arr` (a sorted list), `goal` (the value to search for), and `compare_fn` (a function that compares two elements in the list). The `compare_fn` function should take in two parameters and return a negative number if the first parameter is less than the second, 0 if they are equal, or a positive number if the first parameter is greater than the second. The `binary_search` function should return the index of `goal` if it is present in the list, or -1 if it is not found.
"""

def binary_search(arr, goal, compare_fn):
    """
    Performs a binary search on a sorted list using a custom comparison function.

    Args:
        arr (list): A sorted list of elements.
        goal: The value to search for.
        compare_fn (function): A function that compares two elements in the list.

    Returns:
        int: The index of the goal value if found, -1 otherwise.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        comparison = compare_fn(arr[mid], goal)

        if comparison == 0:
            return mid
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1

    return -1