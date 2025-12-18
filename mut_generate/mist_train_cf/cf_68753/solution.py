"""
QUESTION:
Write a function called `convert_to_ascii` that takes a string as input and returns a new string where all non-alphanumeric characters have been replaced with their ASCII numerical representations.
"""

def convert_to_ascii(text):
    result = ""
    for char in text:
        if not char.isalnum():
            result += str(ord(char))
        else:
            result += char
    return result