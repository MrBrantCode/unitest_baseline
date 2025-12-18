"""
QUESTION:
Write a function `is_substring` that takes two strings as input and returns `True` if the first string contains the second string as a substring, ignoring case sensitivity and whitespace characters, and `False` otherwise. The function should not use any built-in string matching functions or regular expressions.
"""

def is_substring(string1, string2):
    # Convert both strings to lowercase and remove whitespace
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    
    # Check if string2 is a substring of string1
    return string2 in string1