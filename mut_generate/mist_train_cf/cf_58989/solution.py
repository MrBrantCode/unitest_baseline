"""
QUESTION:
Construct a function `find_least_common` that takes a 2D array as input, where the 2D array contains a total of m arrays (1 <= m <= 100), and each individual array n contains (1 <= n <= 1000) integers. The function should return an array with the five least common elements from the input 2D array.
"""

from collections import Counter
from itertools import chain

def find_least_common(array2d):
    # Flattens the 2d array
    flat_list = list(chain(*array2d))

    # Counts the frequency of each item
    counter = Counter(flat_list)

    # Returns the five least common elements
    return [item for item, count in counter.most_common()[:-6:-1]]