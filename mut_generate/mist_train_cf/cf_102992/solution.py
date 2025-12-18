"""
QUESTION:
Create a function that accesses an element at a given index in a list and handles potential exceptions. The function should use a custom exception class that inherits from the base Exception class. If an exception occurs, it should print an error message. The function should not use any built-in exception types other than Exception.
"""

class CustomException(Exception):
    """A custom exception class that inherits from the base Exception class."""
    pass

def access_element(arr, i):
    """
    Access an element at a given index in a list and handle potential exceptions.
    
    Args:
    arr (list): The input list.
    i (int): The index of the element to access.
    
    Returns:
    The element at the given index if it exists.
    """
    try:
        return arr[i]
    except Exception as e:
        raise CustomException("Error: Index out of range") from e