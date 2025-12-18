"""
QUESTION:
Create a function named `join_strings` that takes two parameters: a list of strings and a delimiter character. The function should concatenate all the strings in the list using the delimiter and return the resulting string. The time complexity of the function should be O(n), where n is the total number of characters in all the strings combined. If the input list is empty, the function should return an empty string.
"""

def join_strings(strings, delimiter):
    if not strings:
        return ""

    result = strings[0]
    for i in range(1, len(strings)):
        result += delimiter + strings[i]

    return result