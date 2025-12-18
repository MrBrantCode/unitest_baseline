"""
QUESTION:
Write a function named `count_strings_with_vowels` that takes a list of strings as input and returns a dictionary. The function should count the occurrences of strings that contain at least one vowel and do not start with a capital letter. It should consider vowels from all languages and ignore vowels with accents as separate vowels. The time complexity of the solution should be O(n), where n is the length of the input list of strings.
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