"""
QUESTION:
Write a function `count_substring_occurrences` that takes a string as input and returns a dictionary with the case-insensitive count of all substrings (assuming substrings are separated by spaces) in the string. The function should convert the input string to lowercase before counting the occurrences.
"""

def count_substring_occurrences(string):
    string = string.lower()
    substrings = string.split()
    counts = {}
    for substring in substrings:
        if substring in counts:
            counts[substring] += 1
        else:
            counts[substring] = 1
    return counts