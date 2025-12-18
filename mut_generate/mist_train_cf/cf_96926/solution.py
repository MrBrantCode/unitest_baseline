"""
QUESTION:
Implement a function named `sort_strings` that takes a list of strings as input and returns the sorted list. The strings should be ordered by their lengths in descending order. In cases where multiple strings have the same length, they should be ordered alphabetically. The function should have a time complexity of O(n log n), where n is the length of the input list, and constant space complexity.
"""

def sort_strings(strings):
    return sorted(strings, key=lambda x: (-len(x), x))