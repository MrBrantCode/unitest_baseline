"""
QUESTION:
Write a function `count_characters` that takes an ASCII string `word` as input and returns a dictionary where the keys are the distinct non-vowel alphabetic characters in the string and the values are their corresponding frequencies. The function should ignore non-alphabetic characters and vowels.
"""

from collections import Counter

def count_characters(word):
    counts = Counter(word)
    vowel_counts = {i : counts[i] for i in counts if i not in "aeiouAEIOU" and i.isalpha()}
    return vowel_counts