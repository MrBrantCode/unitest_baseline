"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input, converts them to lowercase, removes duplicates, counts the frequency of each string, and returns a list of strings sorted in descending order of their frequencies. In case of ties, the strings should be sorted lexicographically in ascending order. The function should not use any built-in functions for sorting or counting frequencies.
"""

def sort_strings(strings):
    # Convert all strings to lowercase
    strings = [string.lower() for string in strings]
    
    # Remove duplicates
    strings = list(set(strings))
    
    # Count the frequency of each string
    frequencies = {}
    for string in strings:
        if string in frequencies:
            frequencies[string] += 1
        else:
            frequencies[string] = 1
    
    # Sort the strings by frequency (descending) and lexicographic order (ascending)
    sorted_strings = sorted(frequencies.keys(), key=lambda string: (-frequencies[string], string))
    
    return sorted_strings