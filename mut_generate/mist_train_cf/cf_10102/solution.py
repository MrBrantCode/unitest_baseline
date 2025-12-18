"""
QUESTION:
Implement a function `sort_keys(json_obj)` that takes a JSON object as input and returns a new object with the same keys and values, but with the keys sorted in descending order based on the following criteria: 

1. Key length (longer keys come first)
2. Alphabetical order (if keys have the same length)
3. Number of vowels in the key (more vowels come first, if keys have the same length and alphabetical order)
4. Number of consonants in the key (more consonants come first, if keys have the same length, alphabetical order, and number of vowels)
"""

def sort_keys(json_obj):
    def count_vowels(key):
        vowels = "aeiou"
        return sum(1 for char in key.lower() if char in vowels)

    def count_consonants(key):
        vowels = "aeiou"
        return sum(1 for char in key.lower() if char.isalpha() and char not in vowels)

    sorted_keys = sorted(json_obj.keys(), key=lambda x: (-len(x), x, count_vowels(x), count_consonants(x)))
    return {key: json_obj[key] for key in sorted_keys}