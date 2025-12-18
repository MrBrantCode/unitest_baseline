"""
QUESTION:
Write a function `get_odd_occurrences` that takes a list of integers as input and returns a new list with only the elements that occur an odd number of times. The output list should be in descending order. The function should be able to handle large lists (up to 1 million elements) efficiently.
"""

from collections import Counter

def get_odd_occurrences(lst):
    # Count occurrences of each element
    counts = Counter(lst)
    
    # Filter for elements that occur an odd number of times, sort in descending order
    return [item for item, count in sorted(counts.items(), reverse=True) if count % 2 == 1]