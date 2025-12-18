"""
QUESTION:
Implement a function named `sort_and_remove_duplicates` that takes a list of integers as input, removes duplicates, and returns the sorted list in descending order. The function should not use any external libraries or modules.
"""

def sort_and_remove_duplicates(input_list):
    """
    Removes duplicates from a list of integers and returns the sorted list in descending order.
    
    Parameters:
    input_list (list): A list of integers.
    
    Returns:
    list: The sorted list in descending order with duplicates removed.
    """
    return sorted(list(set(input_list)), reverse=True)