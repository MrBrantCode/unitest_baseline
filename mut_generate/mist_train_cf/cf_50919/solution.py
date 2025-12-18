"""
QUESTION:
Write a function `is_super_happy(s)` that determines if a given string `s` is 'super happy'. A string is 'super happy' if it meets the following conditions:
- It has a length of at least 6 characters.
- Each group of 3 consecutive characters is non-repetitive.
- The whole string is made up of the same distinct group of three letters repeating.
- Each unique character appears at least three times and is not an outlier, meaning its frequency is a multiple of 3.

The function should return `True` if the string is 'super happy' and `False` otherwise.
"""

def is_super_happy(s: str) -> bool:
    # check the length constraint
    if len(s) < 6:
        return False
    # check if each group of 3 consecutive characters are non-repetitive
    # and the whole string is made up of the same distinct group of three letters repeating
    distinct_substrings = set(s[i:i+3] for i in range(0, len(s), 3))
    if len(distinct_substrings) != 1:
        return False
    # check if each unique character appears at least three times and is not an outlier
    char_freq = {char: s.count(char) for char in set(s)}
    return all(freq >= 3 and freq % 3 == 0 for freq in char_freq.values())