"""
QUESTION:
Write a function `compute_lengths` that takes a list of strings as input and returns two values: a list of individual string lengths and the combined length of all strings in the list. The function must not use the built-in `len()` function or any other built-in methods that return the length of a string. The function should accurately handle lists containing duplicates or special characters.
"""

def compute_lengths(lst):
    total_length = 0
    individual_lengths = []
    for string in lst:
        string_length = 0
        for char in string:
            string_length += 1
        individual_lengths.append(string_length)
        total_length += string_length
    return individual_lengths, total_length