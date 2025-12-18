"""
QUESTION:
Write a function `sum_list_recursive(lst)` that calculates the sum of elements in a given list using recursion. The function should handle lists containing positive and negative integers, floating-point numbers, empty lists, and lists with nested sublists. If the list contains strings, the function should return an error message indicating that the list contains invalid elements.
"""

def sum_list_recursive(lst):
    """
    This function calculates the sum of elements in a given list using recursion.
    
    It handles lists containing positive and negative integers, floating-point numbers, 
    empty lists, and lists with nested sublists. If the list contains strings, 
    the function returns an error message indicating that the list contains invalid elements.

    Args:
        lst (list): A list of numbers or nested lists of numbers.

    Returns:
        float: The sum of the elements in the list, or an error message if the list contains strings.
    """

    # Base case: If the list is empty, return 0
    if not lst:
        return 0
    
    # If the first element is a list, recursively call the function on that sublist
    if isinstance(lst[0], list):
        return sum_list_recursive(lst[0]) + sum_list_recursive(lst[1:])
    
    # If the first element is not a number, return an error message
    if not isinstance(lst[0], (int, float)):
        return "Error: List contains invalid elements."
    
    # If the first element is a number, add it to the sum of the rest of the list
    return lst[0] + sum_list_recursive(lst[1:])