"""
QUESTION:
Create a function `are_strings_equal` that takes two strings as input, performs a case-sensitive comparison considering whitespace characters, and returns a boolean indicating whether both strings are equal or not. The input strings must not exceed a length of 100 characters, can only contain alphanumeric characters and special characters (!@#$%^&*()), and must ignore any leading or trailing whitespace characters.
"""

def are_strings_equal(string1, string2):
    # Remove leading and trailing whitespace characters
    string1 = string1.strip()
    string2 = string2.strip()

    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False

    # Check if the strings are equal character by character
    for char1, char2 in zip(string1, string2):
        # Check if the characters are alphanumeric or special characters
        if not (char1.isalnum() or char1 in "!@#$%^&*()") or not (char2.isalnum() or char2 in "!@#$%^&*()"):
            return False
        
        # Check if the characters are equal
        if char1 != char2:
            return False

    # If all checks pass, return True
    return True