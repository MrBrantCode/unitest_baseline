"""
QUESTION:
Write a function named `top_three_frequent` that retrieves the top three most frequently occurring non-duplicate elements from a JSON array and returns them as a JSON array. The function should optimize for time and space complexity. The input is a JSON array and the output is a JSON array. The function should be able to handle a large unsorted array.
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