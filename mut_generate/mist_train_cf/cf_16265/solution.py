"""
QUESTION:
Write a function named compare_strings that compares two strings lexicographically. The function should take two parameters, str1 and str2, and return an integer: -1 if str1 is lexicographically less than str2, 1 if str1 is lexicographically greater than str2, and 0 if they are equal. The function should work with strings of any length, handle uppercase letters by converting them to lowercase, and consider non-alphabet characters as less than any alphabet character. The comparison should be done without using any built-in string comparison functions.
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