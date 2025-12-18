"""
QUESTION:
Write a function `get_last_vowel_flanked_consonant(word)` that, given a word, finds the last consonant that is surrounded by vowels from the right side of the word (case sensitive). Do not include consonants at the beginning or end of the word. Return an empty string if no such consonant is found. Assume the input string contains only English letters.
"""

def get_last_vowel_flanked_consonant(word):
    """Given a word, find the last consonant that is surrounded by vowels from the right side of the word (case sensitive). Do not include consonants at the beginning or end of the word. Return an empty string if no such consonant is found. Assume the input string contains only English letters."""

    vowels = set('aeiouAEIOU')
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] in vowels:
            return word[i]
    return ""