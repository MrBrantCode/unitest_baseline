"""
QUESTION:
Implement a function named `binary_search` that performs binary search on a given sorted list of numbers. The function should take in a list `arr` and a target value `target` as input, and return the index of the target element if it is present in the list, or -1 if it is not present. 

The function should have a time complexity of O(log n), where n is the number of elements in the list, and should handle both even and odd-length lists correctly. It should also be able to handle lists with duplicate elements, empty lists, unsorted lists, lists with negative numbers, lists with floating-point numbers, and lists with non-numeric elements. If the list is unsorted or contains non-numeric elements, the function should return an error message.
"""

def binary_search(arr, target):
    """
    Performs binary search on a given sorted list of numbers.

    Args:
        arr (list): A sorted list of numbers.
        target (int/float): The target value to search for.

    Returns:
        int: The index of the target element if it is present in the list, or -1 if it is not present.
        str: An error message if the list is unsorted or contains non-numeric elements.

    """
    # Check if the list is empty
    if not arr:
        return -1

    # Check if the list contains non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        return "Error: List contains non-numeric elements"

    # Check if the list is sorted
    if arr != sorted(arr):
        return "Error: List is not sorted"

    # Initialize the start and end indices
    start = 0
    end = len(arr) - 1

    # Base case: if the start index is greater than the end index, the target is not present
    if start > end:
        return -1

    # Calculate the middle index
    mid = (start + end) // 2

    # Check if the middle element is the target
    if arr[mid] == target:
        return mid

    # If the target is less than the middle element, search the left half of the list
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)

    # If the target is greater than the middle element, search the right half of the list
    else:
        result = binary_search(arr[mid+1:], target)
        return -1 if result == -1 else mid + 1 + result