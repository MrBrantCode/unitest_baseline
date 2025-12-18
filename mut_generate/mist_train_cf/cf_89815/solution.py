"""
QUESTION:
Write a function named `count_fruits` that takes a JSON object as a string input, where the JSON object contains an array of fruits with their type, count, and color. The function should return a dictionary where the keys are the types of fruits and the values are a tuple containing the total count and the most common color of each fruit type. The dictionary should be sorted in descending order based on the count. In case of a tie for the most common color, consider the color that appears first in the JSON object.
"""

import json
from collections import Counter

def count_fruits(json_string):
    data = json.loads(json_string)
    fruits = data['fruits']

    counts = Counter()
    colors = {}

    for fruit in fruits:
        counts[fruit['type']] += fruit['count']
        if fruit['type'] not in colors:
            colors[fruit['type']] = fruit['color']
    
    result = {}
    for fruit_type, count in counts.items():
        result[fruit_type] = (count, colors[fruit_type])

    result = dict(sorted(result.items(), key=lambda x: x[1][0], reverse=True))
    return result