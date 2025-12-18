"""
QUESTION:
Create a function `remove_duplicates_and_get_top5(strings)` that takes a list of strings as input and returns the top 5 most occurring strings in descending order of their counts. If there are multiple strings with the same count, they should be sorted in reverse lexicographical order. The function should be able to handle lists of up to 10^6 strings.
"""

from collections import Counter

def remove_duplicates_and_get_top5(strings):
    string_counts = Counter(strings)
    return sorted(string_counts.items(), key=lambda x: (-x[1], x[0]))[:5]