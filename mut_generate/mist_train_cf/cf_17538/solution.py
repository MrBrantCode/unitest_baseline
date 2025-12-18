"""
QUESTION:
Implement a function named `custom_exception` that raises a custom exception when the given index is out of range. The function should take an array and an index as input. The custom exception should be a class named `CustomException` that inherits from the base `Exception` class. Use a try-except block to catch and print the error message when the index is out of range. The index is considered out of range if it's less than 0 or greater than or equal to the length of the array.
"""

class CustomException(Exception):
    pass

def custom_exception(arr, index):
    """
    Raises a custom exception when the given index is out of range.

    Args:
        arr (list): The input array.
        index (int): The index to check.

    Raises:
        CustomException: If the index is out of range.
    """
    if index < 0:
        raise CustomException("Index cannot be negative")
    if index >= len(arr):
        raise CustomException("Index out of range")
    return arr[index]