"""
QUESTION:
Create a function named `filter_and_sort_list` that accepts a list of strings and a minimum length threshold as parameters. The function should return a new list containing only the strings that have a length greater than or equal to the minimum length threshold, sorted in descending order based on their length. If two strings have the same length, they should be sorted in alphabetical order. Assume the input list contains only strings and the minimum length threshold is a positive integer.
"""

def filter_and_sort_list(strings, min_length):
    return sorted((string for string in strings if len(string) >= min_length), key=lambda x: (-len(x), x))