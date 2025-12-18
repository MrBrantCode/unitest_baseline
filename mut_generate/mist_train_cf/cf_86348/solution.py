"""
QUESTION:
Write a function `remove_characters(strings, characters)` that takes a list of strings `strings` and a set of characters `characters` as inputs, removes all characters in each string that are in the `characters` set, and removes any strings from the list that become empty after removing characters. The function should return an empty list if the input list is empty and should be able to handle non-alphanumeric characters in the `characters` set with a time complexity of O(n*m), where n is the length of `strings` and m is the average length of each string.
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