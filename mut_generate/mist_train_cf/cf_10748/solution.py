"""
QUESTION:
Write a function `process_strings(strings)` that takes a list of strings as an argument. The function should return a new list containing only the strings that consist entirely of alphabetic characters, converted to uppercase, and sorted in descending order by length.
"""

def process_strings(strings):
    return sorted([string.upper() for string in strings if string.isalpha()], reverse=True, key=len)