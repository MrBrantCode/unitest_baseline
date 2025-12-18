"""
QUESTION:
Write a function named `filter_strings_with_a` that takes an array of strings as input and returns a new array containing only the strings that start with the letter "a". If there are no strings starting with "a", return an empty array. The function must handle arrays of any size and strings of any length.
"""

def filter_strings_with_a(strings):
    result = []
    for string in strings:
        if string.startswith("a"):
            result.append(string)
    if len(result) == 0:
        return []
    return result