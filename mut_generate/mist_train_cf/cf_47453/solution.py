"""
QUESTION:
Write a function `reorder(sentence)` that takes a string of words as input, standardizes the casing of each word to lowercase, and reorders the words based on their starting letter. The reordered words should have all words starting with a vowel ('a', 'e', 'i', 'o', 'u') come first in their original order, followed by the remaining words starting with consonants in their original order.
"""

def reorder(sentence):
    words = sentence.lower().split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelsList = [word for word in words if word[0] in vowels]
    consonantsList = [word for word in words if word[0] not in vowels]
    return ' '.join(vowelsList + consonantsList)