"""
QUESTION:
Write a function `spell_with_vowels(word)` that takes a word as input and returns the word spelled using only its vowels. The function should be case-insensitive and only include the vowels 'a', 'e', 'i', 'o', and 'u' in the output.
"""

def spell_with_vowels(word):
    vowels = "aeiou"
    spelled_word = ""

    for char in word:
        if char.lower() in vowels:
            spelled_word += char.lower()

    return spelled_word