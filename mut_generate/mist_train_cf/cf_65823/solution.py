"""
QUESTION:
Create a function named `remove_duplicates` that takes a sequence (`seq`) as input and returns a new list with duplicate elements removed, while maintaining the original order of elements. The function should be efficient for large data sets and work with any hashable type in Python.
"""

def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]