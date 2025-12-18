"""
QUESTION:
Create a function called `reverse_string_ignore_whitespace` that takes a string as input and returns its reverse, ignoring any leading or trailing whitespace characters and treating uppercase and lowercase characters as equal. The function should handle string inputs that contain special characters or numbers without issues.
"""

def reverse_string_ignore_whitespace(string):
    # Remove leading and trailing whitespace
    string = string.strip()

    # Convert string to lowercase
    string = string.lower()

    # Reverse the string using slicing and return
    return string[::-1]