"""
QUESTION:
Create a function named `linear_search` that performs a case-sensitive linear search on a sorted input array in ascending order. The function should take two parameters: a sorted list of elements and a target value. The function should return the index of the target value if found, and a message or indicator if the target value is not present in the array.
"""

def linear_search(arr, target):
    """
    Performs a case-sensitive linear search on a sorted input array in ascending order.

    Args:
        arr (list): A sorted list of elements.
        target: The target value to be searched.

    Returns:
        int: The index of the target value if found.
        str: A message indicating the target value is not present in the array.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return "Target value not found in the array"
    return "Target value not found in the array"