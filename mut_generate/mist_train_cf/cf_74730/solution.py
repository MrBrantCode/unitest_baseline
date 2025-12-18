"""
QUESTION:
Write a function `is_anagram(str1, str2)` that determines whether two input strings are anagrams of each other, disregarding spaces and case sensitivity. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def entance(str1, str2):
    # Removing all spaces and converting to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths of both strings are not equal, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # If sorted strings are equal, they are anagrams.
    return str1 == str2