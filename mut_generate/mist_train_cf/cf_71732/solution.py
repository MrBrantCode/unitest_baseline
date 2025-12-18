"""
QUESTION:
Create a function called `are_anagrams` that takes two string parameters. The function should return True if the strings are anagrams of each other, and False otherwise. The comparison should be case insensitive and ignore non-alphanumeric characters and spaces.
"""

def are_anagrams(phrase1, phrase2):
    return ''.join(sorted([char.lower() for char in phrase1 if char.isalnum()])) == ''.join(sorted([char.lower() for char in phrase2 if char.isalnum()]))