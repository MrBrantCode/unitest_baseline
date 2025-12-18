"""
QUESTION:
Construct a function, is_anagram, that determines whether two input strings are anagrams of each other. The function should have a time complexity of O(1).
"""

def is_anagram(str1, str2):
    """
    This function checks if two input strings are anagrams of each other.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lower case to make the comparison case-insensitive
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove any white spaces from the strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # If the sorted forms of both strings are equal, they are anagrams
    return sorted(str1) == sorted(str2)