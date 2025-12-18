"""
QUESTION:
Write a function `is_happy(s)` that takes a string `s` as input and returns `True` if the string is "happy" and `False` otherwise. A string is considered "happy" if it meets the following conditions:
- The string is at least 3 characters long.
- Each consecutive set of 3 characters are individual.
- Every unique character appears exactly 2 times.
- No character appears thrice in a direct sequence.
- All character sets of 3 or more contain at least 1 vowel.
- The string does not start or end with the same character.
 
Note: Vowels are defined as 'a', 'e', 'i', 'o', 'u'.
"""

def is_happy(s):
    """
    A string is described as happy if it is at least 3 characters long, each consecutive set of 3 characters are individual, 
    every unique character appears exactly twice, and no characters appears thrice in a direct sequence.
    Additionally, the string is happy if all character sets of 3 or more contains at least 1 vowel 
    and the string should not start or end with the same character.
    """
    from collections import Counter
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s) < 3 or s[0] == s[-1]:
        return False
    counter_ = Counter(s)
    for x, u in counter_.items():
        if u != 2:
            return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3 or len(set(s[i:i+3]).intersection(vowels)) < 1:
            return False
    return True