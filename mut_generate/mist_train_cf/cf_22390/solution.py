"""
QUESTION:
Write a function `find_substring(string, substring)` that returns the index of the first occurrence of the substring in the string. The function should match the entire word and be case-insensitive. If the substring is not found in the string, return -1.
"""

def find_substring(string, substring):
    string = string.lower()
    substring = substring.lower()

    words = string.split()

    for i, word in enumerate(words):
        if word == substring:
            return string.find(word)

    return -1