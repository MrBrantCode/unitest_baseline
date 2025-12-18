"""
QUESTION:
Write a function named `reverse_strings` that takes a list of strings as input and returns a new list where each string in the input list is reversed. The function should handle strings containing special characters, numbers, whitespace characters, Unicode characters, and emojis. The function should also handle the case where the input list is empty or contains a single string.
"""

def reverse_strings(strings):
    return [s[::-1] for s in strings]