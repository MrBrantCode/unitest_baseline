"""
QUESTION:
Write a function `top_three_frequent(json_array)` that takes a JSON array as input and returns a JSON array containing the top three most frequently occurring non-duplicate elements in the input array. The function should optimize for time and space complexity. The input array can be large and unsorted.
"""

import json
from collections import Counter

def top_three_frequent(json_array):
    array = json.loads(json_array)
    counter = Counter(array)
    return json.dumps([elem for elem, freq in counter.most_common(3)])