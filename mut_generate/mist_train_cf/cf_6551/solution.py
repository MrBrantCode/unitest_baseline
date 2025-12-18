"""
QUESTION:
Write a function `filter_strings(arr, char)` that takes an array of strings `arr` and a character `char`, and returns an array containing only the strings that start with the given character, ignoring any leading whitespace characters. The time complexity should be O(n), where n is the total number of characters in all the strings combined, and the space complexity should be O(m), where m is the number of strings that start with the given character.
"""

def filter_strings(arr, char):
    result = []
    for string in arr:
        string = string.lstrip()
        if len(string) > 0 and string[0] == char:
            result.append(string)
    return result