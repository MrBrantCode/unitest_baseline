"""
QUESTION:
Design a function `check_consecutive_chars` that takes a list of two strings as input and returns a boolean indicating whether the characters from the second string appear consecutively in the same sequence in the first string, regardless of repeat characters and case sensitivity.
"""

def check_consecutive_chars(lst):
    # converting strings to lower case for case insensitive comparison
    str1, str2 = lst[0].lower(), lst[1].lower()
    return str2 in str1