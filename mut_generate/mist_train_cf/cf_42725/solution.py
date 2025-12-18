"""
QUESTION:
Implement a function `partition_ordered` that takes a list of tuples `tups` and a key function as input. The function should return a list of tuples, where each tuple consists of a key value and a list of tuples having the same key value, ordered by the key value. The function should work with any type of tuple object and key function, and the output list should be ordered by the key value.
"""

from operator import attrgetter

def partition_ordered(tups, key):
    # Sort the input list of tuples based on the key attribute
    tups.sort(key=key)

    # Initialize an empty dictionary to store the partitioned tuples
    partitioned = {}

    # Iterate through the sorted list of tuples
    for tup in tups:
        # Extract the key value using the key function
        key_value = key(tup)

        # If the key value is not in the partitioned dictionary, add it with an empty list
        if key_value not in partitioned:
            partitioned[key_value] = []

        # Append the current tuple to the list corresponding to its key value
        partitioned[key_value].append(tup)

    # Convert the partitioned dictionary into a list of tuples and return it
    return list(partitioned.items())