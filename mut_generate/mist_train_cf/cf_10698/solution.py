"""
QUESTION:
Write a function called `binarySearch` that takes four parameters: `arr` (a list of elements), `low` and `high` (indices representing the current search range), and `x` (the target element to search for). The function should return the index of `x` if it exists in `arr`, or any value indicating its absence. The function must assume that `arr` is sorted in ascending order.
"""

def binarySearch(arr, low, high, x):
    """
    Perform a binary search on a sorted array.

    Parameters:
    arr (list): A sorted list of elements.
    low (int): The starting index of the current search range.
    high (int): The ending index of the current search range.
    x (any): The target element to search for.

    Returns:
    int: The index of x if it exists in arr, or -1 indicating its absence.
    """
    # Check if the current search range is valid
    if high >= low:

        # Calculate the middle index of the current search range
        mid = (high + low) // 2

        # Check if the target element is found
        if arr[mid] == x:
            return mid

        # If the target element is less than the middle element, search the left half
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

        # If the target element is greater than the middle element, search the right half
        else:
            return binarySearch(arr, mid + 1, high, x)

    # If the target element is not found in the current search range
    else:
        return -1