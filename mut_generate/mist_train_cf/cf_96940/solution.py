"""
QUESTION:
Write a function `count_palindromic_anagram_pairs` that takes two strings as input, determines if they are anagrams of each other (ignoring case, non-alphabetic characters, and considering spaces as valid characters), and checks if the anagram pairs are palindromic. The function should return the count of palindromic anagram pairs found.
"""

def count_palindromic_anagram_pairs(s1, s2):
    s1 = ''.join(char for char in s1 if char.isalpha()).lower()
    s2 = ''.join(char for char in s2 if char.isalpha()).lower()

    if sorted(s1) == sorted(s2):
        combined = s1 + s2
        if combined == combined[::-1]:
            return 2
        else:
            return 1
    else:
        return 0