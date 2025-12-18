"""
QUESTION:
Write a function `has_unique_chars` that checks if all characters in a given string are unique. The function should have a time complexity of O(n), where n is the length of the string, and should not use any additional data structures other than those necessary for the function's parameters and return value.
"""

def has_unique_chars(string):
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True