"""
QUESTION:
Create a function `add_strings` that takes two string parameters, removes any leading or trailing whitespace, and returns their concatenation. The function should return an error message if either input string is null or empty. Each input string can contain up to 100 alphanumeric and special characters.
"""

def add_strings(str1, str2):
    # Check if either string is null or empty
    if not str1 or not str2:
        return "Error: Both input strings must not be null or empty."

    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()

    # Concatenate the strings
    return str1 + str2