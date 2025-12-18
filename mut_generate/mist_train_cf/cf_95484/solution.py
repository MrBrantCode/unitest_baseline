"""
QUESTION:
Write a function `modify_string(string)` that takes a string as input, converts all alphabetic characters to lowercase, ignores non-alphabetic characters, and removes duplicate characters. The function should return the modified string.
"""

def modify_string(string):
    modified_string = ""
    for char in string:
        if char.isalpha():
            modified_string += char.lower()
    modified_string = "".join(dict.fromkeys(modified_string))
    return modified_string