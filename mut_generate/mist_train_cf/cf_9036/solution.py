"""
QUESTION:
Write a function called `multiply_recursive` that takes a list of numbers as input and returns a new list where each number is multiplied by 10. The function must use recursion, not iteration.
"""

def multiply_recursive(my_list):
    """
    This function takes a list of numbers as input, multiplies each number by 10, 
    and returns the resulting list using recursion.

    Args:
        my_list (list): A list of numbers.

    Returns:
        list: A new list with each number multiplied by 10.
    """
    if len(my_list) == 0:
        return []
    else:
        return [my_list[0] * 10] + multiply_recursive(my_list[1:])