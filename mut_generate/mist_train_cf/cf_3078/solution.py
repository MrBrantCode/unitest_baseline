"""
QUESTION:
Write a function `is_anagram(sentence1, sentence2)` to determine if two sentences are anagrams of each other, ignoring case, spaces, and punctuation marks. The function should return `True` if `sentence1` and `sentence2` are anagrams, and `False` otherwise. The function should have a time complexity of O(n log n) or less, where n is the length of the longer sentence.
"""

def is_anagram(sentence1, sentence2):
    sentence1 = ''.join(char.lower() for char in sentence1 if char.isalpha())
    sentence2 = ''.join(char.lower() for char in sentence2 if char.isalpha())

    sentence1_sorted = sorted(sentence1)
    sentence2_sorted = sorted(sentence2)

    return sentence1_sorted == sentence2_sorted