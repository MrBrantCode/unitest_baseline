"""
QUESTION:
Extract Distinct Elements in Descending Order of Occurrence

Create a function `extract_distinct_elements` that takes a list of tuples as input, where each tuple contains an element and a corresponding value. The function should return a list of tuples, where each tuple contains a distinct element from the input list and its occurrence count, sorted in descending order of occurrence.

The input list can contain duplicate elements, and the function should ignore the corresponding values in the tuples. The output list should only contain distinct elements and their occurrence counts.

Example input: [('X', 7), ('Y', 9), ('X', 6), ('Z', 1), ('X', 5), ('Y', 2)] 
Example output: [('X', 3), ('Y', 2), ('Z', 1)]
"""

from collections import Counter

def extract_distinct_elements(data_collection):
    """
    Extract distinct elements in descending order of occurrence.

    Args:
    data_collection (list): A list of tuples, where each tuple contains an element and a corresponding value.

    Returns:
    list: A list of tuples, where each tuple contains a distinct element from the input list and its occurrence count, 
          sorted in descending order of occurrence.
    """
    data = [item[0] for item in data_collection]
    counter = Counter(data)
    return sorted(counter.items(), key=lambda item: item[1], reverse=True)