"""
QUESTION:
Write a function named `extract_characters` that takes a string as input and returns a sorted list of the first and last occurring unique alphabetic characters in the string, considering both lowercase and uppercase letters as the same character, and ignoring non-alphabetic characters.
"""

def extract_characters(string):
    # Remove special characters, numbers, and uppercase letters
    cleaned_string = ''.join(char.lower() for char in string if char.isalpha())

    # Find the first and last occurring unique characters
    unique_chars = []
    for char in cleaned_string:
        if char not in unique_chars:
            unique_chars.append(char)

    # Sort and return the characters
    return sorted(unique_chars)