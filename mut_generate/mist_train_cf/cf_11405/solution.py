"""
QUESTION:
Write a function named `is_anagram` that takes two string parameters and returns `True` if the strings are anagrams of each other and `False` otherwise. The function should be case-insensitive, meaning it should treat 'Listen' and 'Silent' as anagrams.
"""

def is_anagram(string1, string2):
    """
    Checks if two strings are anagrams of each other.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Sort the characters in both strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    # Check if the sorted strings are equal
    return sorted_string1 == sorted_string2