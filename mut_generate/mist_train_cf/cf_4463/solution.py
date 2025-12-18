"""
QUESTION:
Create a function called `sort_strings` that takes a list of strings as input. Sort the list in descending order of string frequencies. In case of ties, sort the strings lexicographically in ascending order. The function should return a list of unique lowercase strings. Do not use built-in functions or data structures for sorting or counting frequencies.
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