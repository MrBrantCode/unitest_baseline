"""
QUESTION:
Design a function `count_upper_case_vowels(s)` to calculate the count of uppercase vowel letters present at even indexed positions in the input string `s`. The vowels to consider are A, E, I, O, and U. The index is 0-based, meaning even indexes are positions 0, 2, 4, and so on.
"""

def count_upper_case_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return len([c for i, c in enumerate(s) if c in vowels and i % 2 == 0])