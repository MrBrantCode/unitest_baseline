"""
QUESTION:
Write a function called `join_strings` that takes a list of strings and a character as input, and returns a single string that joins all the strings together using the given character as a separator. The function must have a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def join_strings(strings, character):
    if len(strings) == 0:
        return ""

    result = strings[0]
    for i in range(1, len(strings)):
        result += character + strings[i]

    return result