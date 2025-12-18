"""
QUESTION:
Create a function `compare_strings` that takes two strings as arguments and returns a boolean indicating whether both strings are equal. The function must perform a case-sensitive comparison, consider whitespace characters (except for leading and trailing ones), and ensure that both strings do not exceed a length of 100 characters and only contain alphanumeric characters and special characters such as !@#$%^&*(). The function should also ignore any leading or trailing whitespace characters in the input strings.
"""

def compare_strings(string1, string2):
    # Remove leading and trailing whitespace characters
    string1 = string1.strip()
    string2 = string2.strip()

    # Check if both strings are empty
    if not string1 and not string2:
        return True

    # Check if the lengths of both strings exceed 100 characters
    if len(string1) > 100 or len(string2) > 100:
        return False

    # Check if both strings contain only alphanumeric and special characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(). ')
    if not set(string1).issubset(allowed_chars) or not set(string2).issubset(allowed_chars):
        return False

    # Compare the strings case-sensitively
    return string1 == string2