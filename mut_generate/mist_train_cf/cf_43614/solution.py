"""
QUESTION:
Write a function to return a default string if the input string is empty or None, otherwise return the input string.

Implement this function using a single line of code. The function should take two parameters: the input string and the default string.
"""

def entrance(otherString, defaultString):
    """Return default string if input string is empty or None, otherwise return input string."""
    return defaultString if not otherString else otherString