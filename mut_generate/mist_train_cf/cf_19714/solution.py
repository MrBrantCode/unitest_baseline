"""
QUESTION:
Implement a function `caesar_cipher(string, shift)` that shifts the characters in a string by a specified number of spaces. The function should handle uppercase and lowercase letters, and preserve any special characters or digits. The shift value should be an integer between -100 and 100, and the output should maintain the case sensitivity of the input string. If the shifted character exceeds the limits of the corresponding character set, it should wrap around to the beginning of the character set. The function should also handle Unicode characters correctly and support a wider range of character sets.
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