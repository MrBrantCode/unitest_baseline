"""
QUESTION:
Write a function `get_closest_vowel(word)` that takes a string `word` as input, containing only English letters, and returns the nearest vowel that is surrounded by two consonants, starting from the right side of the word, while being case-sensitive. Ignore vowels at the beginning or end of the word. If no such vowel exists, return an empty string.
"""

def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in reversed(range(1, len(word) - 1)): 
        if (word[i] in vowels) and (word[i - 1] not in vowels) and (word[i + 1] not in vowels):
            return word[i]
    return ''