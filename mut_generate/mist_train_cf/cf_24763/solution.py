"""
QUESTION:
Write a function called `max_distinct_values` that calculates the maximum number of distinct values that can be inserted into a binary tree with a given number of nodes. The function should return the result as an integer. Assume the binary tree is initially empty and the nodes are added one by one, with each node having a unique value.
"""

def max_distinct_values(n):
    """
    Calculate the maximum number of distinct values that can be inserted into a binary tree with a given number of nodes.
    
    Parameters:
    n (int): The number of nodes in the binary tree.
    
    Returns:
    int: The maximum number of distinct values that can be inserted.
    """
    return 2 ** n - 1