"""
QUESTION:
Write a recursive function `encode_utf8` that takes in a string of up to 100 characters and returns the number of bytes required to encode the string into UTF-8, following the standard UTF-8 encoding rules, with a time complexity of O(n) and a space complexity of O(1).
"""

def entrance(string):
    if len(string) == 0:
        return 0

    char = ord(string[0])
    if char <= 0x7F:
        return 1 + entrance(string[1:])
    elif char <= 0x7FF:
        return 2 + entrance(string[1:])
    else:
        return 3 + entrance(string[1:])