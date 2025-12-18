"""
QUESTION:
Create a function called `get_phrase_syllable_count` that takes a string of English words as input and returns the total number of syllables in the phrase. The function should apply a heuristic approach to estimate syllable count by counting vowels in each word and subtracting silent vowels. If the result is less than 1, return a minimum count of 1.
"""

import re

def get_phrase_syllable_count(phrase):
    vowel_regex = r'[aeiouy]'
    silent_vowel_regex = r'e[bcdfghjklmnpqrstvwxyz]*$'
    words = phrase.split(' ')
    syllable_count = sum(max(1, len(re.findall(vowel_regex, word, re.IGNORECASE)) - len(re.findall(silent_vowel_regex, word, re.IGNORECASE))) for word in words)
    
    return syllable_count