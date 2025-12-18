"""
QUESTION:
Implement a function called `opposite_string` that takes a string as input and returns a new string where each character is replaced by its opposite, defined as the character 13 positions away in the alphabet, wrapping around from the end of the alphabet to the beginning if necessary. The function should handle both uppercase and lowercase characters and leave non-alphabet characters unchanged.
"""

def opposite_string(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
        else:
            result += char
    return result