"""
QUESTION:
Write a recursive function `squares_of_array` that takes a 2D array as input and returns a new 2D array where each element is the square of the corresponding element in the input array. The input array is a list of lists, where each inner list contains numbers. The function should handle nested lists of arbitrary depth.
"""

def squares_of_array(arr):
    """
    This function takes a 2D array as input and returns a new 2D array 
    where each element is the square of the corresponding element in the input array.
    
    Args:
        arr (list): A 2D list of lists containing numbers.
    
    Returns:
        list: A 2D list where each element is the square of the corresponding element in the input array.
    """

    # Base case: if empty
    if not arr:
        return []

    # Recursive case: if it is a list, apply function to each element
    if isinstance(arr[0], list):
        return [squares_of_array(arr[0])] + squares_of_array(arr[1:])

    # Base case: if it is a single element (number), return the square
    return [arr[0]**2] + squares_of_array(arr[1:])