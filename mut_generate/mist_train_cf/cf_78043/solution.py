"""
QUESTION:
Create a function called `sort_by_type_frequency` that takes a list of mixed data types as input and returns the list sorted by the frequency of each data type, with the data types having the highest frequency appearing first. The function should preserve the original order of items with the same type.
"""

import collections

def sort_by_type_frequency(lst):
    # Create a dictionary to store frequency of each type
    type_freq = collections.Counter(type(x) for x in lst)

    # Sort types by their frequency
    sorted_types = sorted(type_freq.keys(), key=lambda x: -type_freq[x])

    # Sort the list based on the sorted types
    sorted_lst = sorted(lst, key=lambda x: sorted_types.index(type(x)))

    return sorted_lst