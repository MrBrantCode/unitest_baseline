"""
QUESTION:
Create a function `top_three_frequent(json_array)` that takes a JSON array as input, and returns a JSON array containing the top three most frequently occurring non-duplicate elements. The function should optimize for both time and space complexity. The input JSON array is a large unsorted array, and the output should be in JSON data format.
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