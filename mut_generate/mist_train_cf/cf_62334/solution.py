"""
QUESTION:
Write a function named `are_characters_unique` that takes a string as input and returns True if all characters in the string are unique and False otherwise. The function must have a time complexity of O(n) where n is the length of the input string. The string can contain spaces and ASCII characters.
"""

def are_characters_unique(in_str):
    in_str = in_str.replace(' ', '')  # remove spaces
    return len(set(in_str)) == len(in_str)