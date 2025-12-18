"""
QUESTION:
Write a function `is_happy(s)` that determines whether a given string `s` meets the "happy criteria." The string must have a length of at least 3, each trio of consecutive characters must be unique, every unique character must appear at least twice, there must be no successive repeating letters, and the total occurrence of each unique character must be an even number. Implement this function using a hash map (dictionary) and a set.
"""

def is_happy(s):
    if len(s) < 3:
        return False

    unique_chars = set(s)
    for char in unique_chars:
        if s.count(char) < 2 or s.count(char) % 2 != 0:
            return False

    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True