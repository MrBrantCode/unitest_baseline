"""
QUESTION:
Find the last occurrence of a specific character in a string.

Create a function named `find_last_occurrence` that takes two parameters: a string and a character. The function should return the index of the last occurrence of the character in the string. If the character is not found, return -1. The solution should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string manipulation methods or additional data structures. The function should be case-sensitive and handle empty strings and strings with only one character appropriately.
"""

def find_last_occurrence(string, character):
    """
    Finds the index of the last occurrence of a character in a string.

    Args:
        string (str): The input string to search in.
        character (str): The character to search for.

    Returns:
        int: The index of the last occurrence of the character. Returns -1 if the character is not found.
    """

    last_occurrence = -1
    for i in range(len(string)-1, -1, -1):
        if string[i] == character:
            last_occurrence = i
            break
    return last_occurrence