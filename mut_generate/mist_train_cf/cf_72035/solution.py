"""
QUESTION:
Write a function `generate_histogram(lst)` that takes a list of strings `lst` and returns a dictionary where the keys are the unique letters in the strings and the values are their respective counts, ignoring case and non-alphabetical characters.
"""

def generate_histogram(lst):
    histogram = {}

    for word in lst:
        for char in word.lower():
            if char.isalpha():
                histogram[char] = histogram.get(char, 0) + 1

    return histogram