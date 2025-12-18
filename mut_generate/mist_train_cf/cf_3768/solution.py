"""
QUESTION:
Print all elements in a given list without using a for loop and achieve a time complexity better than O(n). Ensure the solution uses constant space complexity.
"""

def printing_all_elements(lst):
    """
    Prints all elements in a given list using recursion.
    
    Args:
        lst (list): The list of elements to be printed.
    
    Returns:
        None
    """
    if not lst:
        return
    print(lst[0])
    printing_all_elements(lst[1:])