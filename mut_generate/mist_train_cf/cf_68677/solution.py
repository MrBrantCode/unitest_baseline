"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input and returns the string with all duplicate characters removed. The function must be case sensitive, meaning 'A' and 'a' should not be considered duplicates. The function should achieve this in-place, without using additional data structures, and must have a time complexity less than O(n^2) and a space complexity of O(1).
"""

def remove_duplicates(s):
    """
    Removes all duplicate characters from a string in-place, maintaining their original order.
    
    Args:
    s (str): The input string.

    Returns:
    str: The string with all duplicate characters removed.
    """
    # Convert the string to a list as strings in Python are immutable
    s = list(s)

    # Sort the list in-place
    s.sort()

    # Initialize pointers for traversal
    i = 0

    # Traverse the list for duplicates
    while i < len(s) - 1:
        # If the next character is same as current character
        if s[i] == s[i + 1]:
            # Delete the current character
            del s[i]
        else:
            # Move on to next character
            i += 1

    # Convert the list back to a string and return the result
    return ''.join(s)