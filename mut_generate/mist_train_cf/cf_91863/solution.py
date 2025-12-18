"""
QUESTION:
Write a function `filter_strings_with_the` that takes a list of strings as input and returns a new list containing only the strings that do not contain the word "the" (case insensitive). The function should ignore case sensitivity when comparing strings.
"""

def filter_strings_with_the(strings):
    return [string for string in strings if "the" not in string.lower()]