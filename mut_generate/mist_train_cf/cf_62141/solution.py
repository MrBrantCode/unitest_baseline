"""
QUESTION:
Write a function `are_anagrams(phrase1, phrase2)` that determines if two input phrases are anagrams, disregarding spaces and special characters. The function should be case-insensitive and consider only alphanumeric characters. It should return `True` if the phrases are anagrams and `False` otherwise.
"""

def are_anagrams(phrase1, phrase2):
    p1 = ''.join(filter(str.isalnum, phrase1)).lower()
    p2 = ''.join(filter(str.isalnum, phrase2)).lower()
    return sorted(p1) == sorted(p2)