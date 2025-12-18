"""
QUESTION:
Write a function `get_closest_vowel(word)` that finds the closest vowel to the end of a word that is between two consonants. The function should consider case sensitivity and only examine English alphabets. Vowels at the start or end of the word should be ignored. If no such vowel exists, return an empty string.
"""

def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    word = word[::-1]
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ""