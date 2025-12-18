"""
QUESTION:
Implement a function `good_words(words)` that takes a list of lowercase words as input and returns a list of words containing at least one vowel ('a', 'e', 'i', 'o', 'u') and one consonant (any lowercase letter except for the vowels). The function should preserve the original order of the words and return an empty list if the input list is empty.
"""

def good_words(words):
    def has_vowel_and_consonant(word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        has_vowel = any(char in vowels for char in word)
        has_consonant = any(char not in vowels and char.isalpha() for char in word)
        return has_vowel and has_consonant

    return [word for word in words if has_vowel_and_consonant(word)]