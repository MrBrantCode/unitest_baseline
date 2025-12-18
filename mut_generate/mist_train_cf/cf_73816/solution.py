"""
QUESTION:
Write a function named `sum_numbers` that takes a list as input and returns the sum of all numbers in the list. The list may contain integers, strings, floats, and nested lists up to 3 levels deep. The function should be able to handle nested lists with mixed data types and ignore non-numeric types.
"""

def sum_numbers(lst):
    """
    Recursively calculates the sum of all numbers in a list, 
    including nested lists up to 3 levels deep.
    
    Args:
    lst (list): A list containing integers, strings, floats, and nested lists.
    
    Returns:
    float: The sum of all numbers in the list.
    """
    total = 0
    for i in lst:
        if type(i) == list: 
            total += sum_numbers(i)
        elif isinstance(i, (int, float)): 
            total += i
    return total