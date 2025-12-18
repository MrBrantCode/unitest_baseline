"""
QUESTION:
Create a function called `compare_strings` that takes two strings as input, removes leading and trailing spaces from both strings, and compares them in a case-insensitive manner. The function should return an error message if either string is empty after removing spaces, contains only numbers, or contains special characters. If both strings pass these checks, the function should compare them after converting to lowercase and return a message indicating whether the strings are equal or not.
"""

import string

def compare_strings(s1, s2):
    s1 = s1.strip()
    s2 = s2.strip()
    
    if len(s1) == 0 or len(s2) == 0:
        return "Error: One or both strings are empty."
    if s1.isdigit() or s2.isdigit():
        return "Error: One or both strings contain only numbers."
    if any(char in string.punctuation for char in s1) or any(char in string.punctuation for char in s2):
        return "Error: One or both strings contain special characters."
    
    s1 = s1.lower()
    s2 = s2.lower()
    
    if s1 == s2:
        return "The strings are equal."
    else:
        return "The strings are not equal."