"""
QUESTION:
Create a function `filter_by_prefix_suffix(strings, prefix, suffix)` that filters out strings from an input list `strings` that start with a specific `prefix` and end with a specific `suffix`. The function should use an efficient algorithm with a time complexity of less than O(n^2), where n is the size of the input list.
"""

def filter_by_prefix_suffix(strings, prefix, suffix):
    return [s for s in strings if s.startswith(prefix) and s.endswith(suffix)]