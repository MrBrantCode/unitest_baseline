"""
QUESTION:
Write a function named `get_top_5_common_strings` that takes a list of strings as input, returns the top 5 most common strings that contain at least one uppercase letter and one lowercase letter, and does not consider the order of strings when determining commonality.
"""

from collections import defaultdict
from operator import itemgetter

def get_top_5_common_strings(strings):
    string_counts = defaultdict(int)

    for string in strings:
        if any(char.islower() for char in string) and any(char.isupper() for char in string):
            string_counts[string] += 1

    sorted_counts = sorted(string_counts.items(), key=itemgetter(1), reverse=True)
    top_5_common_strings = [string for string, _ in sorted_counts[:5]]

    return top_5_common_strings