"""
QUESTION:
Create a function `is_anagram(str1, str2)` that determines whether two input strings are anagrams of each other. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the length of the strings.
"""

def is_anagram(str1, str2):
    """
    Determines whether two input strings are anagrams of each other.

    Args:
    str1 (str): The first string to compare.
    str2 (str): The second string to compare.

    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)