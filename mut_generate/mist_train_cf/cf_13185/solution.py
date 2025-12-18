"""
QUESTION:
Write a function `compare_strings` that compares two input strings without using built-in comparison functions or any loops. The function should return True if the strings are equal and False otherwise.
"""

def compare_strings(s1, s2):
    """
    Compares two input strings without using built-in comparison functions or any loops.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
    
    Returns:
        bool: True if the strings are equal, False otherwise.
    """
    return len(s1) == len(s2) and all(s1[i] == s2[i] for i in range(len(s1)))