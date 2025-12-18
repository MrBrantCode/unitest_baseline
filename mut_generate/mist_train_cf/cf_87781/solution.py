"""
QUESTION:
Write a function `is_anagram(sentence1, sentence2)` that determines if two sentences are anagrams of each other. The function should return `True` if `sentence1` and `sentence2` are anagrams, and `False` otherwise. The anagram check should be case-insensitive and ignore spaces and punctuation marks. The function should handle sentences with different lengths and have a time complexity of O(n log n) or less, where n is the length of the longer sentence.
"""

def is_anagram(sentence1, sentence2):
    sentence1 = ''.join(char.lower() for char in sentence1 if char.isalpha())
    sentence2 = ''.join(char.lower() for char in sentence2 if char.isalpha())
    
    return sorted(sentence1) == sorted(sentence2)