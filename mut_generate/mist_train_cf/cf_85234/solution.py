"""
QUESTION:
Write a function `count_upper` that calculates the quantity of uppercase vowels located exclusively in even indices of an input string.
"""

def count_upper(s: str) -> int:
    def is_upper_vowel(c: str) -> bool:
        return c in {'A', 'E', 'I', 'O', 'U'}

    return sum(1 for i in range(0, len(s), 2) if is_upper_vowel(s[i]))