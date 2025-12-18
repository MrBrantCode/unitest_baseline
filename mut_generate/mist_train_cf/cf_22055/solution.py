"""
QUESTION:
Write a function `encode_utf8` that calculates the number of bytes required to encode a given string into UTF-8. The input string can have up to 100 characters. Follow the UTF-8 encoding rules and ensure the function has a time complexity of O(n) and space complexity of O(1), where n is the number of characters in the string.
"""

def encode_utf8(s):
    def utf8_bytes(char):
        if char <= 0x7F:
            return 1
        elif char <= 0x7FF:
            return 2
        else:
            return 3

    return sum(utf8_bytes(ord(char)) for char in s)