"""
QUESTION:
Create a function named 'clean_string' that takes a string as input, removes all non-alphanumeric characters, removes duplicate characters, and returns the modified string in ascending order of characters. The function should be case-insensitive, treating uppercase and lowercase letters as the same character, and should return an empty string if the input string is empty or contains no valid characters.
"""

def clean_string(input_string):
    if not input_string or not any(c.isalnum() for c in input_string):
        return ""

    cleaned_string = ''.join(c.lower() for c in input_string if c.isalnum())
    unique_chars = list(set(cleaned_string))
    sorted_chars = sorted(unique_chars)
    modified_string = ''.join(sorted_chars)

    return modified_string