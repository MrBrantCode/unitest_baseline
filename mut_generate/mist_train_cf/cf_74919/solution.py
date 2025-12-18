"""
QUESTION:
Create a function `replace_chars_with_ascii` that takes a string input and replaces all non-alphabetic characters with their respective ASCII codes in hexadecimal. If a non-alphabetic character is repeated, replace it with the & symbol instead. ASCII codes should be printed in uppercase for hexadecimal representation. The function should only replace each non-alphabetic character with its ASCII code once.
"""

def replace_chars_with_ascii(string: str) -> str:
    replaced_chars = {}
    result = ""
    for char in string:
        if not char.isalpha():
            if char not in replaced_chars:
                replaced_chars[char] = True
                result += hex(ord(char))[2:].upper()
            else:
                result += "&"
        else:
            result += char
    return result