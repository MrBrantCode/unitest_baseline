"""
QUESTION:
Write a function called `remove_chars` that takes two parameters: `string` and `chars`. The function should remove all characters in the string that are in the set of characters `chars`, ignoring case sensitivity. If the input string is empty, the function should return an empty string. The function should be able to handle inputs where `chars` contains non-alphanumeric characters.
"""

def remove_chars(string, chars):
    if not string:
        return ""
    chars = set(chars.lower())
    return "".join(char for char in string if char.lower() not in chars)