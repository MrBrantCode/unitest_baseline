"""
QUESTION:
Create a function `detect_character_type(char)` that takes a single character as input and returns its Unicode category if the character is within the Unicode Supplementary Multilingual Plane (SMP) range (0x10000 to 0x10FFFF). The function should handle invalid inputs (non-Unicode characters or characters outside the SMP range) by returning an error message. The function should have a time complexity of O(log n), where n is the number of characters in the SMP range.
"""

import unicodedata

def detect_character_type(char):
    try:
        code_point = ord(char)
        if 0x10000 <= code_point <= 0x10FFFF:
            category = unicodedata.category(char)
            return category
        else:
            return "Invalid character: outside SMP range"
    except TypeError:
        return "Invalid character: not a unicode character"