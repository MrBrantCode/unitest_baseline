"""
QUESTION:
Implement a function named `reverse_string` that takes a string `s` as input and reverses it in-place without using any built-in functions or methods that directly reverse the string. The solution should have a time complexity of O(n) and handle Unicode characters and very long strings efficiently. Note that strings in Python are immutable, so a conversion to a mutable data structure like a list may be required.
"""

def reverse_string(s):
    """
    Reverse the input string `s` in-place without using any built-in functions or methods that directly reverse the string.
    The solution has a time complexity of O(n) and correctly handles Unicode characters and very long strings efficiently.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    s = list(s)
    length = len(s)
    for i in range(length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
    return "".join(s)