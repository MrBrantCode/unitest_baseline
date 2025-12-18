"""
QUESTION:
Create a function `convert_case(s)` that takes a string `s` as input and returns a string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase without using any built-in string methods or libraries.
"""

def convert_case(s):
    converted = ""
    for char in s:
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:  # uppercase letters
            converted += chr(ascii_val + 32)
        elif 97 <= ascii_val <= 122:  # lowercase letters
            converted += chr(ascii_val - 32)
        else:
            converted += char
    return converted