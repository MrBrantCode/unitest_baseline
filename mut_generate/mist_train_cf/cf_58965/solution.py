"""
QUESTION:
Write a function named `check_anagrams` that takes two strings as input and returns True if they are case-sensitive lexical anagrams, considering special characters but ignoring spaces, and False otherwise.
"""

def check_anagrams(str1, str2):
    # Remove spaces from the strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Check if the sorted strings are equal
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False