"""
QUESTION:
Implement the function `remove_whitespace` that takes a string as input and returns the string with all whitespace characters removed, while maintaining the original order of the characters. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def remove_whitespace(string):
    result = string.replace(" ", "")  # remove whitespace
    return result