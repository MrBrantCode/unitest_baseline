"""
QUESTION:
Create a function `get_unique_combinations` that takes a JSON object containing nested arrays as input. The function should decode the JSON data, obtain all unique elements within the arrays, and generate all unique combinations of two elements from the obtained data. It should then create a hashmap data structure that records the frequency of each combination, considering the ordering of elements within a combination to be irrelevant. Finally, the function should return the combinations and their frequencies.

The input JSON object is expected to be a dictionary where each value is a list of integers. The function should handle any number of arrays in the input JSON and any number of elements within each array. The output should be a hashmap where the keys are the combinations (tuples of two integers) and the values are their corresponding frequencies.
"""

import json
import itertools
from collections import Counter

def get_unique_combinations(data):
    # Create a flat list by combining all arrays
    combined = [item for sublist in data.values() for item in sublist]

    # Create all unique combinations
    combinations = list(itertools.combinations(set(combined), 2))

    # Create a Counter object to hold the counts
    counts = Counter()

    # Increment the count for each combination
    for combination in combinations:
        counts[tuple(sorted(combination))] += 1

    return dict(counts)