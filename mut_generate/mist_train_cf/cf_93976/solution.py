"""
QUESTION:
Write a function named `find_substring_occurrences` that takes two parameters, `string` and `substring`, and returns the starting and ending indices of each occurrence of the `substring` in the `string` and the total number of occurrences found. The function should return the result as a tuple, where the first element is a list of tuples containing the starting and ending indices, and the second element is the total number of occurrences.
"""

import re

def find_substring_occurrences(string, substring):
    occurrences = []
    count = 0

    pattern = re.compile(substring)
    matches = pattern.finditer(string)

    for match in matches:
        start = match.start()
        end = match.end() - 1
        occurrences.append((start, end))
        count += 1

    return occurrences, count