"""
QUESTION:
Implement a function named `compare_strings` that takes two strings as arguments. The function should compare the strings and return True if they are equal (disregarding case sensitivity and ignoring leading, trailing, and excess middle white space) and False otherwise.
"""

def compare_strings(str1, str2):
    # Remove leading and trailing whitespaces and excess middle white space.
    # Also convert both strings to lower case to ignore case sensitivity.
    str1 = " ".join(str1.lower().split())
    str2 = " ".join(str2.lower().split())

    return str1 == str2