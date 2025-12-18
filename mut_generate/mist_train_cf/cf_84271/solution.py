"""
QUESTION:
Write a function `isOneEditDistance(s, t)` that returns `true` if strings `s` and `t` are one edit distance apart and the inserted, deleted, or replaced character is a vowel (a, e, i, o, u, A, E, I, O, U), otherwise return `false`.

Restrictions:
- The function should handle strings `s` and `t` with lengths between 0 and 10^4.
- Strings `s` and `t` consist of lower-case letters, upper-case letters and/or digits.
- The function should return `true` if exactly one of the following operations can be performed on `s` to get `t`: insert a vowel into `s`, delete a vowel from `s`, or replace a character in `s` with a different vowel.
"""

def isOneEditDistance(s, t):
    if abs(len(s) - len(t)) > 1:
        return False
    VOWELS = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if len(s) == len(t):
                return s[i+1:] == t[i+1:] and s[i] in VOWELS and t[i] in VOWELS
            elif len(s) < len(t):
                return s[i:] == t[i+1:] and t[i] in VOWELS
            else:
                return s[i+1:] == t[i:] and s[i] in VOWELS
    if abs(len(s) - len(t)) == 1:
        bigger = s if len(s) > len(t) else t
        return bigger[-1] in VOWELS
    return False