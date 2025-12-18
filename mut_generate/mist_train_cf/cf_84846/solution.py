"""
QUESTION:
Write a function `checkRecord(s)` that takes a string `s` of length `1 <= s.length <= 1000` as input where each character is either `'A'`, `'L'`, or `'P'`. The function should return `True` if the string meets both of the following criteria and `False` otherwise:

- The string contains strictly fewer than 2 `'A'` characters.
- The string does not contain 3 or more consecutive `'L'` characters.
"""

def checkRecord(s):
    return s.count('A') < 2 and s.count('LLL') == 0