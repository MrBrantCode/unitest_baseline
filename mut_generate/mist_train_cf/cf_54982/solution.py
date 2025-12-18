"""
QUESTION:
Implement a function named `is_happy` that determines if a given string is "happy". A string is considered happy if it meets the following conditions:
- The string is at least 3 characters long.
- Each consecutive set of 3 characters are distinct.
- Every unique character appears at least twice.
- No character appears three times in a direct sequence.
- All character sets of 3 or more characters contain at least 1 vowel.
- The string does not start or end with the same character.
"""

def is_happy(s):
    """
    A string is considered happy if it meets the following conditions:
    - The string is at least 3 characters long.
    - Each consecutive set of 3 characters are distinct.
    - Every unique character appears at least twice.
    - No character appears three times in a direct sequence.
    - All character sets of 3 or more characters contain at least 1 vowel.
    - The string does not start or end with the same character.

    :param s: Input string
    :return: True if string is happy, False otherwise
    """
    from collections import Counter
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s) < 3 or s[0] == s[-1]:
        return False
    counter = Counter(s)
    for k, v in counter.items():
        if v < 2:
            return False
    for i in range(len(s)-2):
        if len(set(s[i:i+3])) != 3 or len(set(s[i:i+3]).intersection(vowels)) < 1:
            return False
    return True