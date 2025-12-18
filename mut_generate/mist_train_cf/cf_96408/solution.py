"""
QUESTION:
Implement a function named `count_occurrences` that recursively iterates over a list of items and returns a dictionary with the count of each item as its value. The function should have a time complexity of O(n) and cannot use built-in functions like `count()` or `Counter`. The function should take a list and an optional dictionary as input, with the dictionary defaulting to an empty dictionary if not provided.
"""

def count_occurrences(lst, counts={}):
    if not lst:
        return counts

    item = lst[0]
    counts[item] = counts.get(item, 0) + 1

    return count_occurrences(lst[1:], counts)