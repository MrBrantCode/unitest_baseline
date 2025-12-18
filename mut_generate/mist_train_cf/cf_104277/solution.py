"""
QUESTION:
Write a function named `count_lowercase_chars` that calculates the total number of lowercase characters in a given string, ignoring any whitespace and special characters. The function should take a string as input and return the count of lowercase characters as an integer.
"""

def count_lowercase_chars(s):
    return sum(1 for c in s if c.islower())