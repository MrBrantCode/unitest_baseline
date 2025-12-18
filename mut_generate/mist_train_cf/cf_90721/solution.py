"""
QUESTION:
Create a function `remove_chars` that takes a string and a set of characters as inputs, removes all characters in the string that are in the set (ignoring case sensitivity), and returns the modified string. The function should handle empty input strings and sets containing non-alphanumeric characters.
"""

def remove_chars(string, chars):
    if not string:
        return ""
    chars = set(chars.lower())
    return "".join(char for char in string if char.lower() not in chars)