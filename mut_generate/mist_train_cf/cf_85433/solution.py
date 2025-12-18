"""
QUESTION:
Create a function `merge_sets_and_count` that takes two sets as arguments and returns a dictionary. Each unique value from the sets will be a key in this result dictionary, and the values will be the number of occurrences of this value in both sets. The function should handle both numeric and string values within sets.
"""

def merge_sets_and_count(set1, set2):
    merged = list(set1) + list(set2)
    return {i: merged.count(i) for i in set(merged)}