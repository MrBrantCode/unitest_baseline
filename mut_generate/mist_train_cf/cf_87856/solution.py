"""
QUESTION:
Write a recursive function `calculate_sum` that calculates the sum of the numbers in a given list, including any nested lists, without using any built-in sum() function or any loop structure, with a time complexity of O(n), where n is the length of the list. The function should round floating-point numbers to the nearest integer before adding them to the sum.
"""

def calculate_sum(lst):
    """
    This function calculates the sum of the numbers in a given list, 
    including any nested lists, without using any built-in sum() function or any loop structure.

    Args:
    lst (list): The input list containing numbers and/or nested lists.

    Returns:
    int: The sum of the numbers in the list.
    """
    if not lst: 
        return 0
    
    total_sum = 0
    
    # Base case: if the first item in the list is a number, add it to total_sum
    if isinstance(lst[0], float):
        total_sum += round(lst[0])
    elif isinstance(lst[0], int):
        total_sum += lst[0]
    
    # If the first item is a list, recursively call calculate_sum on it
    if isinstance(lst[0], list):
        total_sum += calculate_sum(lst[0])
    
    # Recursive case: call calculate_sum on the rest of the list
    total_sum += calculate_sum(lst[1:])
    
    return total_sum