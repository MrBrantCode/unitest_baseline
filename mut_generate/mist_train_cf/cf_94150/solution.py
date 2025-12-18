"""
QUESTION:
Implement a function `compare_strings(str1, str2)` that compares two strings lexicographically. The function should return -1 if `str1` is less than `str2`, 1 if `str1` is greater than `str2`, and 0 if the strings are equal. The comparison should be case-insensitive and consider non-alphabet characters as less than any alphabet character. The function should not use any built-in string comparison functions and should work efficiently for strings of any length.
"""

def compare_strings(str1, str2):
    str1 = str1.lower()  # Convert to lowercase
    str2 = str2.lower()

    # Iterate over each character of the strings
    for i in range(min(len(str1), len(str2))):
        # Compare the characters
        if str1[i] < str2[i]:
            return -1
        elif str1[i] > str2[i]:
            return 1

    # If one string is a prefix of the other, the longer string is considered greater
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1

    # The strings are equal
    return 0