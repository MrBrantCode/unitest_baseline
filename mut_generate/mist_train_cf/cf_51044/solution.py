"""
QUESTION:
Create a function named `homogenize_text(text)` that takes a string as input and returns a modified string where all spaces are removed, all characters are converted to lowercase, and all non-alphanumeric characters are replaced with underscores.
"""

def homogenize_text(text):
    result = ''
    for char in text:
        if char.isalnum():
            result += char.lower()
        elif char.isspace():
            continue
        else:
            result += '_'
    return result