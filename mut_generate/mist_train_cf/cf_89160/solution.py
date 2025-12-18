"""
QUESTION:
Write a function named `parse_string` that takes a string as input and returns a dictionary where each key is a letter or number from the string and its corresponding value is the frequency of that character in the string. The function should be case sensitive, ignore characters that are not letters or numbers, exclude characters with a frequency less than 2, and return the dictionary in descending order of frequency.
"""

import collections

def parse_string(string):
    counter = collections.Counter()
    for char in string:
        if char.isalnum():
            counter[char] += 1
    counter = {char: freq for char, freq in counter.items() if freq >= 2}
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return counter