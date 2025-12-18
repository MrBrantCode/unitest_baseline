"""
QUESTION:
Write a function `get_closest_vowel(word)` that finds the closest vowel situated between two consonants in a word, not including vowels at the beginning or end of the word, from the right side. The function should be case sensitive and consider vowel combinations that represent a single sound. If no such vowel is found, return an empty string. Assume the input string contains only English letters.
"""

def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    combinations = {'ea', 'ou', 'EE'}
    for cur, nxt in zip(word[1:-1], word[2:]):
        if cur + nxt in combinations:
            return cur + nxt
        elif cur in vowels and nxt not in vowels:
            return cur
    return ""