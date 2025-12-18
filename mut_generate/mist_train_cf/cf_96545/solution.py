"""
QUESTION:
Write a function `reverse_strings` that takes a list of strings as input, reverses the order of each string in the list without using built-in string reverse functions or methods, and stores the reversed strings in the original list, without using loops or recursion.
"""

def reverse_strings(lst):
    """
    Reverses the order of each string in the list without using built-in string reverse functions or methods.
    
    Args:
        lst (list): A list of strings.
    
    Returns:
        list: The list with the order of each string reversed.
    """
    return [word[::-1] for word in lst]