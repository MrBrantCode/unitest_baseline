"""
QUESTION:
Write a function `sort_lowercase_letters` that takes a string as input and returns a new string with the same lowercase letter count in ascending order of their ASCII values. The function should only consider lowercase alphabets and ignore any other characters, including uppercase alphabets and non-alphabetic characters.
"""

def sort_lowercase_letters(string):
    lowercase_letters = [char for char in string if char.islower()]
    sorted_letters = sorted(lowercase_letters, key=lambda x: ord(x))
    return ''.join(sorted_letters)