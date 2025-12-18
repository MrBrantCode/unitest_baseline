"""
QUESTION:
Create a function `replicate_list` that takes two parameters: a list and an integer. The function should return a new list that replicates the original list's content the specified number of times. For example, replicating the list ["a", "b", "c"] three times would result in ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'].
"""

def replicate_list(original_list, n):
    """
    This function replicates the original list's content the specified number of times.
    
    Parameters:
    original_list (list): The list to be replicated.
    n (int): The number of times the list should be replicated.
    
    Returns:
    list: A new list that replicates the original list's content the specified number of times.
    """
    return original_list * n