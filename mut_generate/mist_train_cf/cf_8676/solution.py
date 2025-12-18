"""
QUESTION:
Create a method `remove_duplicate_chars` that takes a string as input, removes all duplicate characters while maintaining the original order, and returns the resulting string. The method should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions or regular expressions. The method should handle both uppercase and lowercase characters as distinct characters, Unicode characters in addition to ASCII characters, and should only use variables and basic operations on characters.
"""

def remove_duplicate_chars(s):
    """
    Removes all duplicate characters from a string while maintaining the original order.

    Args:
        s (str): The input string.

    Returns:
        str: The string with all duplicate characters removed.

    Time complexity: O(n), where n is the length of the input string.
    """
    result = ""
    seen = set()
    for c in s:
        if c not in seen:
            result += c
            seen.add(c)
    return result