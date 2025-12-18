"""
QUESTION:
Write a function called `convert_to_integers` that takes a list of strings representing integers and returns a list of integers. The input list will only contain strings that can be successfully converted to integers.
"""

def convert_to_integers(arr):
    """
    This function takes a list of strings representing integers and returns a list of integers.
    
    Parameters:
    arr (list): A list of strings representing integers.
    
    Returns:
    list: A list of integers.
    """
    return list(map(int, arr))