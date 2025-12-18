"""
QUESTION:
Create a function `are_anagrams(str1, str2)` that determines whether two input strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def are_anagrams(str1, str2):
    """
    Determine whether two input strings are anagrams of each other.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(str1) == sorted(str2)