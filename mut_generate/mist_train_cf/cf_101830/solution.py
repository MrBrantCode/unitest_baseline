"""
QUESTION:
Write a function called `top_three_frequent` that takes a JSON array as input and returns the top three most frequently occurring non-duplicate elements as a JSON array. The function should be optimized for both time and space complexity. The input JSON array is assumed to be a large unsorted array, and the function should handle this scenario efficiently.
"""

import json
from collections import Counter

def top_three_frequent(json_array):
    # convert JSON array to Python list
    array = json.loads(json_array)
    
    # create Counter object
    counter = Counter(array)
    
    # return top three elements as JSON array
    return json.dumps([elem for elem, freq in counter.most_common(3)])