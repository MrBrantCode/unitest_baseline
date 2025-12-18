"""
QUESTION:
Write a function named `longest_common_suffix` that takes a list of strings as input and returns the longest common suffix among all strings. The function should handle lists with any number of strings, strings of varying lengths, and different character compositions.
"""

def longest_common_suffix(strings):
    if not strings:
        return ""

    suffix = reversed(strings[0])

    for i, char in enumerate(suffix):
        for string in strings:
            if i >= len(string) or string[-i - 1] != char:
                return strings[0][-i:]

    return strings[0]