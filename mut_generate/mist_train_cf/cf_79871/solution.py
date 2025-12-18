"""
QUESTION:
Create a function `process_list` that takes a list of numbers as input, squares the even numbers, cubes the odd numbers, and replaces any non-integer values with 0. The function should return the resulting list.
"""

def process_list(input_list):
    """
    This function takes a list of numbers, squares the even numbers, cubes the odd numbers, 
    and replaces any non-integer values with 0.

    Args:
        input_list (list): A list of numbers.

    Returns:
        list: The resulting list after applying the operations.
    """
    result = []
    for i in input_list:
        if isinstance(i, int):  
            if i % 2 == 0:  
                result.append(i ** 2)
            else:  
                result.append(i ** 3)
        else:  
            result.append(0)
    return result