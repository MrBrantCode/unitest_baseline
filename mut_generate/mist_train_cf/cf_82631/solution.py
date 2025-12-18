"""
QUESTION:
Develop a function `rarest_elements` that takes a list as input and returns a list of tuples. Each tuple contains an element from the input list and its relative frequency, calculated as the count of the element divided by the total count of elements in the list. The function should return all elements with the lowest frequency. If the input list is empty, the function should return an empty list.
"""

from collections import Counter

def entance(lst):
    if not lst:
        return []

    counter = Counter(lst)
    min_count = min(counter.values())
    rarest_items = [(item, count / len(lst)) for item, count in counter.items() if count == min_count]

    return rarest_items