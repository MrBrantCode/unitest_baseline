"""
QUESTION:
Write a function named `generate_composition` that takes two parameters: `theme` and `rhyme_pattern`. The function should return a list of four distinct words that maintain a cohesive theme and follow a specified pattern of rhyming. The `theme` parameter should be one of the keys in the `themes` dictionary, and the `rhyme_pattern` parameter should be one of the keys in the `rhyme_patterns` dictionary. The function should handle exceptions and return an empty list if any error occurs.
"""

import random

themes = {
    "love": ["love", "dove", "above", "glove"],
    "nature": ["sea", "be", "free", "tree"]
}

rhyme_patterns = {
    "AABB":["0,1,2,3"],
    "ABAB":["0,2,1,3"],
    "ABBA":["0,3,2,1"],
}

def generate_composition(theme, rhyme_pattern):
    try:
        theme_words = themes[theme]
        pattern = rhyme_patterns[rhyme_pattern]
        ordered_indexes = [int(i) for i in pattern[0].split(',')]

        composition = [theme_words[i] for i in ordered_indexes]
    except Exception as e:
        print(f'Exception occurred: {e}')
        print(traceback.format_exc())
        return []
        
    return composition