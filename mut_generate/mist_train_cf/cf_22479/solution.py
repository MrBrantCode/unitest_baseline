"""
QUESTION:
Write a function called `remove_duplicates` that takes a string as input and returns a new string where all duplicate characters have been removed while preserving the original order of characters. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the string.
"""

def remove_duplicates(string):
    """
    Removes duplicate characters from a string while preserving the original order of characters.

    Args:
        string (str): The input string.

    Returns:
        str: A new string with all duplicate characters removed.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    unique_chars = set()
    result = ""
    
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    
    return result