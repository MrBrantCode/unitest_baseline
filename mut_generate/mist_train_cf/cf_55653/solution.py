"""
QUESTION:
Write a function `is_anagram` that takes two strings as input. The function should determine whether the two input strings are anagrams of each other, considering capital and lowercase letters as distinct characters and ignoring any spaces in the strings. Return `True` if the strings are anagrams, `False` otherwise.
"""

def is_anagram(s1, s2):
    # Remove spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # Check if lengths of two strings are same, if not, they cannot be Anagrams
    if len(s1) != len(s2):
        return False

    # Sort the strings and check if they are same
    return sorted(s1) == sorted(s2)