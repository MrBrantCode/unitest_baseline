"""
QUESTION:
Write a method named `is_substring` that takes two strings as input and returns `True` if the first string contains the second string as a substring, ignoring case sensitivity and whitespace characters. The method should not use any built-in string matching functions or regular expressions.
"""

def is_substring(s1, s2):
    # Convert both strings to lowercase and remove whitespace
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # Check if s2 is a substring of s1
    return s2 in s1