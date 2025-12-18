"""
QUESTION:
Design a function `count_syllables` that takes a string as input and returns the total number of syllables in the string. The function should consider full-word syllables only, disregarding silent syllables and punctuation. A 'y' should be considered a syllable only if it is not at the beginning of the word. The function should be optimized for minimal computational resource consumption while ensuring functional accuracy.
"""

import re

def count_syllables(string):
    count = 0
    regex = r'[aiouy]+e*|e(?!d$|ly).|[td]ed|le$|les$'
    words = re.split(r'[\s.,;!?]+', string)
    for word in words:
        word = word.lower()
        syllables = re.findall(regex, word)
        count += len(syllables)
    return count