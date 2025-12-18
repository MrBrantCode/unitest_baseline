"""
QUESTION:
Write a function `is_anagram_of_palindrome(s)` that takes a string `s` as input and returns `True` if `s` is an anagram of any palindrome and `False` otherwise. The input string is assumed to contain only lower-case English letters with no spaces.
"""

def is_anagram_of_palindrome(s):
    frequencies = dict()
    for c in s:
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1

    odd_count = 0
    for value in frequencies.values():
        if value % 2 != 0:  
            if odd_count == 1: 
                return False
            else:
                odd_count += 1
    return True