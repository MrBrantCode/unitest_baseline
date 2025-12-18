"""
QUESTION:
Given a list of tuples, where each tuple contains a string and an integer, write a function named `unpack_tuples` that takes this list as input and returns two separate lists: one for the strings and one for the integers.
"""

def unpack_tuples(tuples):
    """
    This function takes a list of tuples as input, where each tuple contains a string and an integer.
    It returns two separate lists: one for the strings and one for the integers.
    
    Args:
        tuples (list): A list of tuples, each containing a string and an integer.
    
    Returns:
        tuple: Two separate lists, the first for the strings and the second for the integers.
    """
    names, ages = zip(*tuples)
    return list(names), list(ages)