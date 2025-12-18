"""
QUESTION:
Write a function `is_substring` that checks if a given string (`string2`) is a substring of another string (`string1`), ignoring case and any leading or trailing spaces. The function should return a boolean value indicating whether `string2` is a substring of `string1`.
"""

def is_substring(string1, string2):
    # Remove leading and trailing spaces
    string1 = string1.strip()
    string2 = string2.strip()

    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Check if string2 is a substring of string1
    return string2 in string1