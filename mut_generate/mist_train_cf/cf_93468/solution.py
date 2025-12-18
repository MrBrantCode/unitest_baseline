"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns the number of character positions at which the strings differ from each other, ignoring case and leading/trailing whitespaces, and handling Unicode characters properly.
"""

def compare_strings(str1, str2):
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    return sum(1 for char1, char2 in zip(str1, str2) if char1 != char2)