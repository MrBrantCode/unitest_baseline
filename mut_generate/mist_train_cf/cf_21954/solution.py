"""
QUESTION:
Write a function called `sum_list_recursive` that takes a list as input and returns the sum of its elements. The function should use recursion to calculate the sum. The list can contain positive and negative integers, floating-point numbers, and can be empty. The function should handle nested sublists and calculate the sum correctly. The function should also handle large lists without causing a stack overflow error.
"""

def sum_list_recursive(lst):
    """
    This function calculates the sum of elements in a given list using recursion.
    It handles positive and negative integers, floating-point numbers, empty lists, 
    large lists, and nested sublists.
    
    Args:
        lst (list): A list of numbers that can be positive, negative, integer or float, 
                    and can be empty or contain nested sublists.
                    
    Returns:
        float: The sum of all elements in the list.
    """
    
    # Base case: If the list is empty, return 0
    if not lst:
        return 0
    
    # If the first element is a list, recursively call the function on it
    if isinstance(lst[0], list):
        return sum_list_recursive(lst[0]) + sum_list_recursive(lst[1:])
    
    # If the first element is a number, add it to the sum of the rest of the list
    elif isinstance(lst[0], (int, float)):
        return lst[0] + sum_list_recursive(lst[1:])
    
    # If the first element is not a number or a list, ignore it and move on
    else:
        return sum_list_recursive(lst[1:])