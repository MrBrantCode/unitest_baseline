"""
QUESTION:
Write a function `expand_strings` that takes a list of strings as input and returns a list of tuples. Each tuple contains an original string and its corresponding set of characters, but only if the string contains at least one vowel and no special characters or numbers. The resulting list of tuples should be sorted in descending order based on the number of vowels in each set.
"""

def expand_strings(strings):
    expanded_strings = []

    for string in strings:
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        
        vowels = set(char.lower() for char in string if char.lower() in 'aeiou')
        if len(vowels) == 0:
            continue
        
        expanded_strings.append((string, vowels))

    expanded_strings.sort(key=lambda x: len(x[1]), reverse=True)
    return expanded_strings