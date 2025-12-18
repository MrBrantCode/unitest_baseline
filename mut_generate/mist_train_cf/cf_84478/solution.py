"""
QUESTION:
Write a function `is_happy(s, n)` that takes a string `s` and an integer `n` as input, where `1 <= n <= len(s)`. The function should return `True` if the string is happy and `False` otherwise. A string is happy if it has at least `n+2` characters, at least 2 unique characters, every `n` consecutive letters are distinct, and every distinct letter appears at least twice.
"""

def is_happy(s, n):
    if len(set(s)) < 2:
        return False

    unique_chars = set(s)
    char_counts = {char: 0 for char in unique_chars}

    for i in range(len(s) - n):
        if len(set(s[i:i + n])) != n:
            return False
        for char in s[i:i + n]:
            char_counts[char] += 1

    for count in char_counts.values():
        if count < 2:
            return False

    return True