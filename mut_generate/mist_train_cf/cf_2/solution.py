"""
QUESTION:
Write a function `remove_spaces_and_punctuation(s)` that removes spaces and punctuation marks from a given string `s` and returns the modified string, containing only the alphanumeric characters (uppercase and lowercase letters, digits) without any spaces or punctuation marks, with a time complexity of O(n), where n is the length of the input string, and without using any built-in string manipulation functions or regular expressions.
"""

def remove_spaces_and_punctuation(s):
    result = ""
    for char in s:
        ascii_value = ord(char)
        if (ascii_value >= 48 and ascii_value <= 57) or (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
            result += char
    return result