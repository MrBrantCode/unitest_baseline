"""
QUESTION:
Write a function `duplicate_characters` that finds all duplicate characters in a given string. The function should return a set of characters that appear more than once in the string. The function should have a time complexity of O(n), where n is the length of the string. The function should not use Python's built-in `count` function or list comprehensions that include the `count` method.
"""

def duplicate_characters(string):
    char_counts = {}
    duplicate = set()
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
            duplicate.add(char)  # Add to the set as it's a duplicate
        else:
            char_counts[char] = 1
    return duplicate