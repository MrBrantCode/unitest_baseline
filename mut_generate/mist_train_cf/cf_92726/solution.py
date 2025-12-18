"""
QUESTION:
Write a function named `count_characters(s1, s2)` that takes two strings `s1` and `s2` as input and returns the total count of characters in `s2` that are present in `s1`. The function should be case-sensitive and should count each occurrence of the characters in `s2` separately. The strings `s1` and `s2` can contain any printable ASCII characters, including letters, digits, symbols, and whitespace.
"""

def count_characters(s1, s2):
    count = 0
    for char in s2:
        count += s1.count(char)
    return count