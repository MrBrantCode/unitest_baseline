"""
QUESTION:
Create a function named 'merge_and_sort' that takes two lists of integers as input, merges them into a single list, and returns the merged list in descending order. The function should not modify the input lists.
"""

def merge_and_sort(list_a, list_b):
    """
    This function merges two lists of integers into a single list and returns the merged list in descending order.
    
    Parameters:
    list_a (list): The first list of integers.
    list_b (list): The second list of integers.
    
    Returns:
    list: The merged list in descending order.
    """
    merged_list = list_a + list_b
    return sorted(merged_list, reverse=True)