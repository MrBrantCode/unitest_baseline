"""
QUESTION:
Write a function `is_anagram` that takes two strings as input and returns `True` if they are anagrams of each other, and `False` otherwise. The function should ignore case, consider whitespace and punctuation marks as part of the comparison, and handle potential exceptions such as `None` inputs.
"""

def is_anagram(string1, string2):
    # Check if either string is None
    if string1 is None or string2 is None:
        return False

    # Remove whitespace and punctuation marks
    string1 = ''.join(e for e in string1 if e.isalnum())
    string2 = ''.join(e for e in string2 if e.isalnum())

    # Check if the lengths of the strings are different
    if len(string1) != len(string2):
        return False

    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Check if the sorted strings are equal
    return sorted(string1) == sorted(string2)