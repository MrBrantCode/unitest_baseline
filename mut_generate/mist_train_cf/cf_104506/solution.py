"""
QUESTION:
Write a function `compare_strings` that compares two strings and returns True if they match, considering both case-sensitive and case-insensitive comparisons. The function should take two strings as input, each with a length of 1-1000 characters, consisting only of alphanumeric characters. The function should return True if the strings match in either case-sensitive or case-insensitive comparison, and False otherwise.
"""

def compare_strings(s1, s2):
    return s1 == s2 or s1.lower() == s2.lower()