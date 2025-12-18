"""
QUESTION:
Create a function called `expand_strings` that takes a list of strings as input. Expand each string in the list into a set of characters only if it contains at least one vowel, and sort the resulting sets in descending order based on the number of vowels in each set.
"""

def expand_strings(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    expanded = []
    for string in strings:
        if any(char.lower() in vowels for char in string):
            expanded.append(set(string))
    expanded.sort(key=lambda x: len([char for char in x if char.lower() in vowels]), reverse=True)
    return expanded