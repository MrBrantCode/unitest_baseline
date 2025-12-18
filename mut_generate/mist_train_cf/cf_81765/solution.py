"""
QUESTION:
Create a function `min_consonants` that takes a word as input and returns True if the word contains at least two consonants, and False otherwise. The function should be case-insensitive and consider only alphabetic characters. Use this function to filter a list of words and return a new list containing only the words that meet the condition.
"""

def min_consonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for ch in word.lower() if ch.isalpha() and ch not in vowels) >= 2