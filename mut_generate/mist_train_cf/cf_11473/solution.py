"""
QUESTION:
Implement a function `optimized_loop` that efficiently iterates over the elements of a given multidimensional array and performs an action on the elements that meet a specific condition. The function should take as input a 2D array and a condition function that returns a boolean value indicating whether an element meets the condition. The function should minimize unnecessary iterations and computations.
"""

def optimized_loop(array, condition):
    """
    Efficiently iterates over the elements of a given multidimensional array 
    and performs an action on the elements that meet a specific condition.

    Args:
    array (list): A 2D array.
    condition (function): A function that returns a boolean value indicating 
                         whether an element meets the condition.

    Returns:
    list: A list of elements that meet the condition.
    """
    result = []
    for sub_array in array:
        for element in sub_array:
            if condition(element):
                # Perform the action on the element
                # For demonstration purposes, we'll just append the element to the result list
                result.append(element)
    return result