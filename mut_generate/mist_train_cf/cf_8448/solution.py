"""
QUESTION:
Write a function named `reverse_strings` that takes a list of strings as input and returns a new list where each string in the input list has been reversed. The function should be able to handle strings containing special characters, numbers, whitespace characters, Unicode characters, and emojis. The function should also handle edge cases such as an empty list and a list containing a single string.
"""

def reverse_strings(strings):
    return [s[::-1] for s in strings]