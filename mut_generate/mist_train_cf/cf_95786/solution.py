"""
QUESTION:
Implement a function `caesar_cipher(string, shift)` that takes a string and an integer shift value between -100 and 100 as input, and returns the string with its letters shifted by the specified number of spaces while maintaining case sensitivity and preserving special characters and digits. The shifted characters should wrap around to the beginning of their character set if they exceed the limits, and the function should handle Unicode characters correctly.
"""

def caesar_cipher(string, shift):
    result = ""
    
    for char in string:
        if char.isalpha():
            unicode_offset = ord('A') if char.isupper() else ord('a')
            shifted_unicode = (ord(char) - unicode_offset + shift) % 26 + unicode_offset
            result += chr(shifted_unicode)
        else:
            result += char
    
    return result