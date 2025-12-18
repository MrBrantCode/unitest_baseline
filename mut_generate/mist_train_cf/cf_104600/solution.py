"""
QUESTION:
Write a function `is_permutation` that takes two strings as input and returns a boolean indicating whether one string is a permutation of the other. The function must have a time complexity of O(n log n) due to the sorting operation, where n is the length of the strings. Assume the input strings only contain lowercase letters.
"""

def is_permutation(str1, str2):
    """
    Checks if one string is a permutation of the other.
    
    Args:
    str1 (str): The first string.
    str2 (str): The second string.
    
    Returns:
    bool: True if str1 is a permutation of str2, False otherwise.
    """
    
    # If the lengths of the strings are not equal, they cannot be permutations of each other
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in each string
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    # If the sorted strings are equal, the original strings are permutations of each other
    return str1_sorted == str2_sorted