"""
QUESTION:
Write a function called `filter_strings` that takes an array of strings and a character as input. Return an array containing only the strings that start with the given character, ignoring any leading whitespace characters. The time complexity of your solution should be O(n), where n is the total number of characters in all the strings combined. The space complexity should be O(m), where m is the number of strings that start with the given character.
"""

def filter_strings(arr, char):
    result = []
    for string in arr:
        string = string.lstrip()
        if len(string) > 0 and string[0] == char:
            result.append(string)
    return result