"""
QUESTION:
Implement a recursive function binary_search(array, item) that performs a binary search on a given array to find a specific item. The function should return the index of the item if found, and an error message if the item is not found, the array is empty, or the indices are not integers. The array is assumed to be sorted in ascending order. The function should use recursion instead of a while loop and handle all edge cases.
"""

def binary_search(array, item, low=None, high=None):
    # Check if array is empty
    if not array:
        return "Error: Array is empty"

    # Post-initialization
    if low is None or high is None:
        low = 0
        high = len(array) - 1

    # Check if indices are integers
    if not isinstance(low, int) or not isinstance(high, int):
        return "Error: Indices have to be integers"

    if low <= high:
        mid = (low + high) // 2  # Find the average index (integer division)
        if array[mid] == item:  # Found the item
            return mid
        elif array[mid] > item:  # The item is in the first half of the array
            return binary_search(array, item, low, mid - 1)  # Recursive call on the first half
        else:  # The item is in the second half of the array
            return binary_search(array, item, mid + 1, high)  # Recursive call on the second half
    else:
        # Item not in array
        return "Error: Item not found in the array"