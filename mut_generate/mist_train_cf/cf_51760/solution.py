"""
QUESTION:
Write a function `longest_string(strings, alphabet)` that takes a list of strings `strings` and a list of characters `alphabet` as input. Return the longest string from `strings` that can be formed using each character in `alphabet` at most once. If no such string exists, return an empty string.
"""

def longest_string(strings, alphabet):
    alphabet_set = set(alphabet)
    strings.sort(reverse=True, key=len)
    for string in strings:
        has_all_characters = all(c in alphabet_set for c in string)
        if has_all_characters and len(set(string)) == len(string):
            return string
    return ""