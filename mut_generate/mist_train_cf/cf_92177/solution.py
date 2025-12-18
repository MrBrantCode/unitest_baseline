"""
QUESTION:
Design a function named `reverse_string` that reverses the input string in place without using any additional variables or data structures, such as arrays or lists. The function should take three parameters: the input string (as a list of characters), and two indices `start` and `end` representing the substring to be reversed.
"""

def reverse_string(s, start, end):
    """
    Reverses a substring of the input string in place.

    Args:
        s (list): The input string as a list of characters.
        start (int): The start index of the substring to be reversed.
        end (int): The end index of the substring to be reversed.
    """
    if start >= end:
        return
    # Swap the first and last characters
    s[start], s[end] = s[end], s[start]
    # Reverse the remaining characters
    reverse_string(s, start+1, end-1)