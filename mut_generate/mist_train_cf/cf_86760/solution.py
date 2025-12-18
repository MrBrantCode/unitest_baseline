"""
QUESTION:
Write a function named `has_unique_chars` that takes a string as input and returns `True` if the string has all unique characters and `False` otherwise. Assume the input string only contains ASCII characters and do not use any additional data structures, built-in functions, libraries, or modules, or convert the string into a different data structure. The function should have a time complexity of O(n), where n is the length of the string.
"""

def has_unique_chars(string):
    if len(string) > 128:  
        return False

    char_set = [False] * 128
    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True

    return True