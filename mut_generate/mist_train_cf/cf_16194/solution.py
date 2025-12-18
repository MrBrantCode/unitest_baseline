"""
QUESTION:
Design a function `calculate_string_length` that calculates the length of a given string without using the built-in length function or method. The function should handle strings of any length and complexity, including special characters, numbers, and whitespace, and should be able to handle strings encoded in a specific character encoding format, such as UTF-8 or UTF-16. The function should accurately count the length of the string in terms of the actual number of characters in the encoded form, considering the encoding scheme's rules. The function should take two parameters: `string` and `encoding`, where `encoding` is optional and defaults to 'utf-8'.
"""

def calculate_string_length(string, encoding='utf-8'):
    encoded_string = string.encode(encoding)
    return len(encoded_string)