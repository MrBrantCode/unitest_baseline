"""
QUESTION:
Write a function `find_smallest_missing_integer(retrieved_documents)` that takes a set of integers `retrieved_documents` as input and returns the smallest positive integer that is not present in the set. The function should return an integer value.
"""

def find_smallest_missing_integer(retrieved_documents: set) -> int:
    smallest_missing = 1
    while smallest_missing in retrieved_documents:
        smallest_missing += 1
    return smallest_missing