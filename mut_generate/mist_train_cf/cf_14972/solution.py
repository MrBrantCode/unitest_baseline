"""
QUESTION:
Create a function called `reverse_string_ignore_whitespace` that takes a string as input and returns its reverse. The function should ignore any leading or trailing whitespace characters, be case-insensitive, and handle special characters and numbers.
"""

def reverse_string_ignore_whitespace(s):
    # Remove leading and trailing whitespace
    s = s.strip()

    # Convert string to lowercase
    s = s.lower()

    # Reverse the string using slicing and return
    return s[::-1]