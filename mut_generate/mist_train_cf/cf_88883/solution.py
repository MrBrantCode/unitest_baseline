"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that have at least two occurrences of the letter 'a' and end with the letter 'e'. The returned list should be sorted in descending order based on the number of occurrences of the letter 'a' in each string.
"""

def filter_strings(strings):
    return sorted([string for string in strings if string.count('a') >= 2 and string.endswith('e')], key=lambda x: x.count('a'), reverse=True)