"""
QUESTION:
Write a function are_anagrams(sentence1, sentence2) to determine if two sentences are anagrams of each other. The function should return True if sentence1 and sentence2 are anagrams, and False otherwise. The anagram check should be case-insensitive and ignore spaces and punctuation marks.
"""

import string

def are_anagrams(sentence1, sentence2):
    sentence1 = sentence1.lower().translate(str.maketrans('', '', string.punctuation + ' '))
    sentence2 = sentence2.lower().translate(str.maketrans('', '', string.punctuation + ' '))

    dict1 = {}
    dict2 = {}

    for char in sentence1:
        dict1[char] = dict1.get(char, 0) + 1

    for char in sentence2:
        dict2[char] = dict2.get(char, 0) + 1

    return dict1 == dict2