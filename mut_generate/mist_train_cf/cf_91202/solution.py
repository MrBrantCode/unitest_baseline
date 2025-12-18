"""
QUESTION:
Create a function `sort_keys` that takes a JSON object as input and returns a new JSON object with its keys sorted in the following order of priority: 
- Length of the key in descending order
- Alphabetical order of the key
- Number of vowels in the key in descending order
- Number of consonants in the key in descending order
"""

import json

def sort_keys(json_obj):
    def count_vowels(key):
        vowels = "aeiou"
        return sum(1 for char in key.lower() if char in vowels)

    def count_consonants(key):
        vowels = "aeiou"
        return sum(1 for char in key.lower() if char.isalpha() and char not in vowels)

    sorted_keys = sorted(json_obj.keys(), key=lambda x: (-len(x), x, count_vowels(x), count_consonants(x)))
    return {key: json_obj[key] for key in sorted_keys}