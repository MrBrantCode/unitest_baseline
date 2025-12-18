"""
QUESTION:
Create a function `remove_duplicates_and_get_top5(strings)` that takes a list of strings as input, removes duplicates while preserving the original count of each unique string, and returns the top 5 most occurring strings in descending order of their counts. If multiple strings have the same count, they should be sorted in reverse lexicographical order. The input list can contain up to 10^6 strings.
"""

from collections import Counter

def remove_duplicates_and_get_top5(strings):
    string_counts = Counter(strings)
    top5_strings = sorted(string_counts.items(), key=lambda x: (-x[1], x[0]))
    return top5_strings[:5]