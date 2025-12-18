"""
QUESTION:
Write a function named `minkowski_distance` to compute the Minkowski distance between two lists of up to 10^6 elements, given a parameter p. The function should take in three parameters: two lists of integers and the Minkowski parameter p.
"""

def minkowski_distance(list1, list2, p):
    """
    This function calculates the Minkowski distance between two lists.
    
    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.
    p (int): The Minkowski parameter.
    
    Returns:
    float: The Minkowski distance between the two lists.
    """
    return sum(abs(a - b)**p for a, b in zip(list1, list2)) ** (1. / p)