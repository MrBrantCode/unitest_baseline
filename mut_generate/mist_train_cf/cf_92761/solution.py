"""
QUESTION:
Create a function `spell_with_vowels(word)` that takes a string `word` as input and returns a string containing only the vowels from `word`. The vowels are 'a', 'e', 'i', 'o', and 'u', and the function should be case-insensitive.
"""

def spell_with_vowels(word):
    vowels = "aeiou"
    spelled_word = ""

    for char in word:
        if char.lower() in vowels:
            spelled_word += char.lower()

    return spelled_word