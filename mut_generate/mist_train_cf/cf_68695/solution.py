"""
QUESTION:
Construct a function called `count_consonants` that takes a list of sentences as input. The function should calculate the total count of consonants from the input sentences, excluding sentences that start with a vowel, end with a consonant, contain numbers or special characters, or have fewer than 5 words. The function should be able to handle sentences in different languages.
"""

import re
import unicodedata

def count_consonants(sentences):
    total_consonants = 0
    signs = re.compile(r'[0-9`~!@#$%^&*()_\-+={}:;"\'<>,.?\/\\[\]]')

    def is_consonant(s):
        return unicodedata.category(s)[0] in ("L") and unicodedata.category(s) != 'Ll' \
               and unicodedata.category(s) != 'Lu'

    def is_vowel(s):
        return s.lower() in ('a', 'e', 'i', 'o', 'u')

    for sentence in sentences:
        if signs.search(sentence) or len(sentence.split()) < 5 or sentence == '' or is_vowel(sentence[0]) or is_consonant(sentence[-1]):
            continue
        else:
            for word in sentence.split():
                for letter in word:
                    if is_consonant(letter):
                        total_consonants += 1
    return total_consonants