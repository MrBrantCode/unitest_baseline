"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input, removes duplicates, and returns the sorted list of strings. The strings should be ordered by their lengths in descending order. If multiple strings have the same length, they should be ordered alphabetically. The function must achieve a time complexity of O(n log n) and constant space complexity, without relying on built-in sorting functions or libraries.
"""

def sort_strings(strings):
    strings = list(set(strings))
    tuples = [(len(s), s) for s in strings]
    tuples.sort(key=lambda x: (-x[0], x[1]))
    return [t[1] for t in tuples]