"""
QUESTION:
Write a Python function `expand_strings` that takes a list of strings as input. For each string in the list, if it contains at least one vowel, expand it into a set of characters. The resulting sets should be sorted in descending order based on the number of vowels in each set. Vowels are defined as 'a', 'e', 'i', 'o', and 'u'.
"""

def expand_strings(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    expanded = []
    for string in strings:
        if any(char in vowels for char in string):
            expanded.append(set(string))
    expanded.sort(key=lambda x: len([char for char in x if char in vowels]), reverse=True)
    return expanded