"""
QUESTION:
Implement a function `contains_only_lowercase` that checks if a given string contains only lowercase alphabets. The function should return True if all characters in the string are lowercase alphabets, and False otherwise. The function should have a time complexity of O(n), where n is the length of the string.
"""

def contains_only_lowercase(string):
    for char in string:
        if not char.islower():
            return False
    return True