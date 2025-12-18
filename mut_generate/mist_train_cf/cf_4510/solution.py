"""
QUESTION:
Write a function `count_elements` that takes a variable as input and returns the type of the variable and the total number of elements in the variable. If the variable is a list, it should return 'list' as the type and recursively count the elements in all nested lists. If the variable is not a list, it should return the type of the variable and an error message or a default value for the element count.
"""

def count_elements(lst):
    """
    This function recursively counts the elements in a list, including nested lists.
    
    Args:
    lst (list): The input list to count elements from.
    
    Returns:
    int: The total number of elements in the list.
    """
    count = 0
    for i in lst:
        if isinstance(i, list):
            count += count_elements(i)
        else:
            count += 1
    return count