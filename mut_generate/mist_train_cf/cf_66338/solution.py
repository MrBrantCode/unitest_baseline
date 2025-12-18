"""
QUESTION:
Write a function called `max_vowels` that accepts a list of distinct English words and returns the word with the maximum number of vowel characters (including 'y' as a vowel). The function should return the first word in case of a tie.
"""

def max_vowels(words):
    vowels = 'aeiouyAEIOUY'
    max_vowels_word = max(words, key=lambda x: sum([1 for char in x if char in vowels]))
    return max_vowels_word