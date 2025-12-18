"""
QUESTION:
Write a function `top_three_frequent(json_array)` that takes a JSON-formatted array as input and returns a JSON-formatted array containing the top three most frequently occurring non-duplicate elements in the input array. The function should have a time complexity of O(n) or better and a space complexity of O(n), where n is the size of the input array. The output array should be sorted in descending order of frequency.
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