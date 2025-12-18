"""
QUESTION:
Write a function `string_info` that takes an array of strings as input and returns a set of tuples. Each tuple should contain a string from the original array, its length, and the number of vowels it contains. The function should be case-insensitive when counting vowels.
"""

def string_info(strings):
    result = set()
    for string in strings:
        length = len(string)
        vowels = sum(1 for char in string if char.lower() in 'aeiou')
        result.add((string, length, vowels))
    return result