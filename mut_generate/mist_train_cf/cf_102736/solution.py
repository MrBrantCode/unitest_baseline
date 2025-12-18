"""
QUESTION:
Write a function called `check_unique_chars` that determines if all characters in a given string are unique. The function should return a boolean value (True if all characters are unique, False otherwise) and must have a time complexity of O(n), where n is the length of the string.
"""

def check_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True