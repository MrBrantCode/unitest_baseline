"""
QUESTION:
Write a function named `is_super_happy` that takes a string `s` as input and returns a boolean value indicating whether the string meets certain conditions. The string must have a length of at least 6 characters, it must be composed of the same group of three distinct characters repeating, and each character in the string must appear at least three times and a multiple of three times.
"""

def is_super_happy(s: str) -> bool:
    # check the length constraint
    if len(s) < 6:
        return False
    # Check if each group of 3 consecutive characters are non-repetitive
    # and the whole string is made up of the same distinct group of three letters repeating
    distinct_substrings = set(s[i:i+3] for i in range(0, len(s), 3))
    if len(distinct_substrings) != 1:
        return False
    # Check if each unique character appears at least three times and is not an outlier
    char_freq = {char: s.count(char) for char in set(s)}
    return all(freq >= 3 and freq % 3 == 0 for freq in char_freq.values())