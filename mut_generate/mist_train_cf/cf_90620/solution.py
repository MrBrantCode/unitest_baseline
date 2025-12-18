"""
QUESTION:
Write a function named `count_strings_with_vowels` that takes a list of strings as input and returns a dictionary where the keys are the strings that contain at least one vowel and the values are the counts of how many times each string appears. The function should ignore any strings that start with a capital letter and consider vowels from all languages, treating vowels with accents as the same vowel.
"""

import re

def count_strings_with_vowels(strings):
    vowels = re.compile(r'[aeiou]', re.IGNORECASE)
    counts = {}
    
    for string in strings:
        if string[0].isupper():
            continue
        if vowels.search(string):
            if string in counts:
                counts[string] += 1
            else:
                counts[string] = 1
    
    return counts