"""
QUESTION:
Write a function `remove_characters(strings, characters)` that takes a list of strings `strings` and a set of characters `characters` as inputs, and returns a list of strings where all characters in `characters` are removed from each string in `strings`. If a string becomes empty after removing characters, it should be removed from the list. The function should handle empty input lists and have a time complexity of O(n*m), where n is the length of the list of strings and m is the average length of each string.
"""

def remove_characters(strings, characters):
    if not strings:
        return []

    cleaned_strings = []
    for string in strings:
        cleaned_string = ''.join(char for char in string if char not in characters)
        if cleaned_string:
            cleaned_strings.append(cleaned_string)

    return cleaned_strings