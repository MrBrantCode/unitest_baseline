"""
QUESTION:
Write a function named `odd_occurrences` that takes a nested list of integers as input, where each integer can be repeated in any sublist, and returns a new list containing only the integers that occur an odd number of times in the entire list. The function should handle any number of sublists and any number of integers within each sublist.
"""

from collections import Counter
from itertools import chain

def odd_occurrences(nested_list):
    flat_list = list(chain(*nested_list))
    count_dict = Counter(flat_list)
    return [number for number, count in count_dict.items() if count % 2 != 0]