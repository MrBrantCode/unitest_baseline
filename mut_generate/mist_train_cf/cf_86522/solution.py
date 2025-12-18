"""
QUESTION:
Create a function `contains_substring` that takes two strings, `string1` and `string2`, as input. The function should return `True` if `string1` contains `string2` as a substring, ignoring case sensitivity and whitespace characters. However, the function should return `False` if either string has leading or trailing whitespace characters, or if `string1` contains any special characters (non-alphabetic or non-whitespace characters). Do not use built-in string matching functions or regular expressions.
"""

def contains_substring(string1, string2):
    # Remove leading and trailing whitespace from both strings
    string1 = string1.strip()
    string2 = string2.strip()

    # Check if either string has leading or trailing whitespace
    if string1 != string1.strip() or string2 != string2.strip():
        return False

    # Remove whitespace characters from both strings
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    # Check if any special character is present in the first string
    for char in string1:
        if not char.isalpha() and char != " ":
            return False

    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Check if the second string is a substring of the first string
    if string2 in string1:
        return True
    else:
        return False