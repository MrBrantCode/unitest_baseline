"""
QUESTION:
Write a function `access_and_manipulate_last_element` that takes a dynamically sized array as input and returns the array with its last element manipulated according to a given operation. The function should be able to access and modify the last element directly without knowing the size of the array beforehand. The array can be of any data type and the operation can be any valid array operation.
"""

def access_and_manipulate_last_element(array, operation, value):
    """
    Access and manipulate the last element of a dynamically sized array.

    Args:
    array (list): The input array.
    operation (str): The operation to be performed on the last element.
    value (any): The value used in the operation.

    Returns:
    list: The array with the last element manipulated.
    """
    if operation == 'replace':
        array[-1] = value
    # Add more operations as needed
    return array