"""
QUESTION:
Get the key/index of the current element in a foreach loop in C#. Create a function named `get_key` that takes an array and a search value as input, and returns the key/index of the element that is less than or equal to the search value. The function should stop iterating once the condition is met. Note that this problem is in C#, but a Python solution is provided as an answer.
"""

def get_key(arr, search):
    """
    Returns the key/index of the element that is less than or equal to the search value.

    Args:
        arr (list): A list of elements.
        search (int): The search value.

    Returns:
        int: The key/index of the element that is less than or equal to the search value.
    """
    for i, val in enumerate(arr):
        if search <= val:
            return i
    return None  # Return None if no such element is found