"""
QUESTION:
Write a function `has_unique_chars(string)` to check if the input string contains all unique ASCII characters without using any additional data structures. The function should achieve a time complexity of O(n), where n is the length of the string. Note that the input string only contains ASCII characters.
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