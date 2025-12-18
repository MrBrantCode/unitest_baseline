"""
QUESTION:
Write a function `anagram_to_dict` that takes a string as input and returns a dictionary where the keys are the lowercase alphabetic characters in the string and the values are their corresponding frequencies. The input string may contain non-alphabetic characters and may be in any case. The function should ignore non-alphabetic characters, convert all characters to lowercase, and count the frequency of each alphabetic character.
"""

import string

def anagram_to_dict(anagram):
    anagram = ''.join(c for c in anagram if c.isalpha()).lower()
    return {char: anagram.count(char) for char in set(anagram)}