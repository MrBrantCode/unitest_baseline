"""
QUESTION:
Create a function named `are_anagrams` that determines if two given words are anagrams, considering different letter cases and including non-alphabetic characters. The function should return `True` if the words are anagrams and `False` otherwise.
"""

def are_anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    return sorted(word1) == sorted(word2)