"""
QUESTION:
Write a function named `has_unique_characters` that checks whether a given string has all unique characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. The input string only contains ASCII characters.
"""

def has_unique_characters(string):
    if len(string) > 128:
        return False
    char_set = 0
    for char in string:
        val = ord(char)
        if char_set & (1 << val) > 0:
            return False
        char_set |= 1 << val
    return True