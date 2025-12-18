"""
QUESTION:
Write a function called `are_anagrams` that takes two strings as input and returns `True` if the strings are anagrams of each other and `False` otherwise. The function should ignore the order of characters in the strings and consider only the frequency of each character. The strings are considered anagrams if and only if they contain the same characters with the same frequency.
"""

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)