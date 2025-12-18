"""
QUESTION:
Write a function named `most_frequent_value` that takes a list of elements as input, which can contain up to 1 million elements and can be either strings or integers. The function should return the most frequent element in the list, converted to a string if it is a string, and as an integer otherwise.
"""

from collections import Counter

def most_frequent_value(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0][0]
    return str(most_common) if isinstance(most_common, str) else int(most_common)