"""
QUESTION:
Create a function named `is_alternating` that takes a string `word` as input. The function should return `True` if the word has alternating vowels and consonants (ignoring case), and `False` otherwise. The function should consider only alphabetic characters and should return `False` if the word is empty or has only one character.
"""

def is_alternating(word):
    vowels = "aeiou"
    if not word or len(word) == 1:
        return False
    prev_is_vowel = word[0].lower() in vowels
    for char in word[1:]:
        char = char.lower()
        if char.isalpha() and (char in vowels) == prev_is_vowel:
            return False
        if char.isalpha():
            prev_is_vowel = not prev_is_vowel
    return True