"""
QUESTION:
Write a function called `remove_vowels` that takes a string as input and returns the string with all vowels removed. The function should not use any built-in string manipulation functions or methods. Vowels are case-insensitive, i.e., both lowercase and uppercase vowels should be removed.
"""

def remove_vowels(string):
    return "".join([char for char in string if char.lower() not in ['a', 'e', 'i', 'o', 'u']])