"""
QUESTION:
Write a function called `find_largest_binary` that takes a list of binary strings as input, converts each string to an integer, and returns the largest number from the set. The function should only accept a list of strings where each string represents a binary number.
"""

def find_largest_binary(binary_strings):
    """
    This function takes a list of binary strings, converts each string to an integer, 
    and returns the largest number from the set.
    
    Parameters:
    binary_strings (list): A list of strings where each string represents a binary number.
    
    Returns:
    int: The largest number from the set of binary strings.
    """
    return max(map(lambda x: int(x, 2), binary_strings))