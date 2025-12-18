"""
QUESTION:
Write a function called `change_immutable_tuple` that takes an immutable tuple as an input and returns the modified tuple. The function should attempt to change the first element of the tuple to a specified value.
"""

def change_immutable_tuple(input_tuple, new_value):
    """
    Returns a new tuple with the first element changed to a specified value.
    
    Since tuples are immutable in Python, this function does not modify the original tuple.
    Instead, it creates a new tuple with the desired change.

    Args:
        input_tuple (tuple): The input tuple to be modified.
        new_value: The new value to be assigned to the first element of the tuple.

    Returns:
        tuple: A new tuple with the first element changed to the specified value.
    """
    return (new_value,) + input_tuple[1:]