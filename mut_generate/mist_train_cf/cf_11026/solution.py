"""
QUESTION:
Create a function `remove_whitespace` that takes a string as input and returns the string with all whitespace characters removed, maintaining the original order of characters. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def remove_whitespace(string):
    result = string.replace(" ", "")
    return result