"""
QUESTION:
Write a function `count_substrings` that takes a string as input, splits it into substrings separated by spaces, and returns a dictionary with the frequency of each substring. The function should count the occurrences of each word in the string, where words are separated by spaces. The returned dictionary should have the substrings as keys and their respective counts as values.
"""

def count_substrings(string):
    substr_count = {}
    substrings = string.split()
    for substr in substrings:
        if substr in substr_count:
            substr_count[substr] += 1
        else:
            substr_count[substr] = 1
    return substr_count