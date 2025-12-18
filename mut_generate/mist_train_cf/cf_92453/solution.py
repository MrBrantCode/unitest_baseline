"""
QUESTION:
Create a function named `remove_duplicates_and_sort_desc` that takes a list of numbers as input, removes all duplicated entries, and sorts the remaining numbers in descending order. The input list can contain up to 10^6 elements.
"""

def remove_duplicates_and_sort_desc(num_list):
    """
    Removes duplicates from a list of numbers and sorts the remaining numbers in descending order.
    
    Args:
    num_list (list): A list of numbers.
    
    Returns:
    list: A list of unique numbers sorted in descending order.
    """
    return sorted(set(num_list), reverse=True)