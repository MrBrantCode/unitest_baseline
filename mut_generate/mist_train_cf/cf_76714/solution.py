"""
QUESTION:
Write a function `extract_vowel_words(words_array)` that takes an array of words as input and returns a list of words that consist only of vowels. The function should be case-insensitive and should return an empty list if no words consist only of vowels.
"""

def extract_vowel_words(words_array):
    vowels = set("aeiou")
    vowel_words = []
    for word in words_array:
        if set(word.lower()).issubset(vowels):
            vowel_words.append(word)
    return vowel_words