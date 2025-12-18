"""
QUESTION:
Create a function named `count_unique_characters` that takes a string as input and returns the number of unique characters in the string, treating uppercase and lowercase versions of the same letter as distinct characters, and ignoring whitespace.
"""

def count_unique_characters(s):
    return len(set(s.replace(" ", "")))