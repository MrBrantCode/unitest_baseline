"""
QUESTION:
Write a function named `filter_strings` that takes an array of strings and a character as input, and returns an array containing only the strings that include the given character. The returned strings should be ordered in descending order of their lengths.
"""

def filter_strings(strings, char):
    # Filter the list with strings containing the character 
    filtered_strings = list(filter(lambda x: char in x, strings))

    # Sort the list in descending order of length of strings
    sorted_strings = sorted(filtered_strings, key=len, reverse=True)

    return sorted_strings