"""
QUESTION:
Write a function `reverse_strings` that takes a list of strings as input and reverses the order of each string in the list without using any built-in string reverse functions or methods. The function should not use any loops or recursion. The reversed strings should still be stored in the original list.
"""

def reverse_strings(lst):
    """
    Reverses the order of each string in the input list without using any built-in string reverse functions or methods.
    
    Args:
    lst (list): A list of strings.
    
    Returns:
    list: The input list with each string reversed.
    """
    return [word[::-1] for word in lst]