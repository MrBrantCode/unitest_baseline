"""
QUESTION:
Write a function `longest_unique_string` that takes a list of strings as input and returns the longest string without any repeating characters. The function should not use any built-in string manipulation functions or sorting algorithms. The time complexity should be O(n^2), where n is the total number of characters in all the strings combined, and the space complexity should be O(1).
"""

def longest_unique_string(strings):
    """
    This function finds the longest unique string from a list of strings.

    Args:
    strings (list): A list of strings.

    Returns:
    str: The longest string without repeating characters.
    """

    def is_unique(s):
        """Check if a string is unique."""
        char_set = set()
        for char in s:
            if char in char_set:
                return False
            char_set.add(char)
        return True

    longest = ""
    for s in strings:
        if is_unique(s) and len(s) > len(longest):
            longest = s

    return longest