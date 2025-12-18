"""
QUESTION:
Create a function named `clean_string` that takes a string as input and returns a string containing only the alphabetical characters from the original string.
"""

def clean_string(s):
    output = ""
    for char in s:
        if char.isalpha():
            output += char
    return output