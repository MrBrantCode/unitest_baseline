"""
QUESTION:
Write a function `get_unique_permutations(arr)` that generates all unique permutations of the input array `arr` where characters cases (lowercase and uppercase) are considered unique. The function should also remove any duplicate permutations from the output.

In addition, create a helper function `is_hex_color(s)` that takes a permutation as input and returns a boolean value indicating whether the input string is a valid hexadecimal color code, which starts with '#' and is followed by either 3 or 6 hexadecimal numbers.
"""

from itertools import permutations

def get_unique_permutations(arr):
    """
    Generates all unique permutations of the input array arr where characters cases 
    (lowercase and uppercase) are considered unique.
    
    Args:
        arr (list): The input array of characters.
    
    Returns:
        list: A list of unique permutations.
    """
    unique_permutations = set([''.join(p) for p in permutations(arr)])
    return list(unique_permutations)


def is_hex_color(s):
    """
    Checks if the input string is a valid hexadecimal color code.
    
    A valid hexadecimal color code starts with '#' and is followed by either 3 or 6 hexadecimal numbers.
    
    Args:
        s (str): The input string to be checked.
    
    Returns:
        bool: True if the input string is a valid hexadecimal color code, False otherwise.
    """
    if len(s) != 7 and len(s) != 4:
        return False
    if s[0] != "#":
        return False
    hex_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}
    return all(c in hex_chars for c in s[1:])