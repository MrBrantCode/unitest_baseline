"""
QUESTION:
Write a function `compare_strings(str1, str2)` that compares two input strings and returns `True` if they are the same and `False` otherwise. The comparison should ignore leading or trailing white spaces, case differences, and any non-alphabet characters. You cannot use built-in string comparison functions or regular expressions.
"""

def compare_strings(str1, str2):
    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()

    # Clean the strings
    str1_clean = ''
    for char in str1:
        if char.isalpha():
            str1_clean += char.lower()

    str2_clean = ''
    for char in str2:
        if char.isalpha():
            str2_clean += char.lower()

    # Compare the cleaned strings
    if len(str1_clean) != len(str2_clean):
        return False

    for char1, char2 in zip(str1_clean, str2_clean):
        if char1 != char2:
            return False

    return True