"""
QUESTION:
Write a function `is_substring(string1, string2)` that determines if `string1` contains `string2` as a substring, ignoring case sensitivity and whitespace characters. The function should return `False` if any special character (non-alphabetic or non-whitespace character) is found in `string1`. Do not use built-in string matching functions or regular expressions.
"""

def is_substring(string1, string2):
    # Remove whitespace and convert both strings to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if any special character is present in string1
    for char in string1:
        if not char.isalpha() and not char.isspace():
            return False

    # Check if string2 is a substring of string1
    index = 0
    while index <= len(string1) - len(string2):
        if string1[index:index+len(string2)] == string2:
            return True
        index += 1

    return False