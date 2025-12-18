"""
QUESTION:
Implement a function `replace_punctuation_with_hyphen` that takes a string `para` as input and returns a string where all punctuation marks are replaced with hyphens, and any consecutive hyphens are replaced with a single hyphen. The function should not use any inbuilt string or regex functions for manipulation, instead manually checking each character of the string.
"""

def replace_punctuation_with_hyphen(para):
    punctuation = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', '\'', '"', '<', '>', ',', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '\\', '|', '+', '=']

    result = ''
    last_char_was_hyphen = False

    for char in para:
        if char in punctuation:
            if not last_char_was_hyphen:
                result += '-'
                last_char_was_hyphen = True
        else:
            result += char
            last_char_was_hyphen = False

    return result