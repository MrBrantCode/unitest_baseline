"""
QUESTION:
Create a function named `top_three_frequent` that takes a JSON array as input and returns the top three most frequently occurring non-duplicate elements as a JSON array. The function should be optimized for time and space complexity.
"""

import json
from collections import Counter

def top_three_frequent(json_array):
    array = json.loads(json_array)
    counter = Counter(array)
    return json.dumps([elem for elem, freq in counter.most_common(3)])