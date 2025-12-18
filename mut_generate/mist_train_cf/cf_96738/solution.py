"""
QUESTION:
Write a function `count_fruits` that takes a JSON object as input and returns a sorted dictionary where the keys are the types of fruits and the values are a tuple containing the total count and the most common color of each fruit type. The dictionary should be sorted in descending order based on the count. The most common color is the one with the highest count for each fruit type. In case of a tie, consider the color that appears first in the JSON object.
"""

import json
from collections import defaultdict

def count_fruits(json_data):
    data = json.loads(json_data)
    fruit_counts = defaultdict(lambda: [0, ""])
    
    for fruit in data["fruits"]:
        fruit_type = fruit["type"]
        count = fruit["count"]
        color = fruit["color"]

        fruit_counts[fruit_type][0] += count

        if fruit_counts[fruit_type][1] == "" or count > fruit_counts[fruit_type][0]:
            fruit_counts[fruit_type][1] = color

    sorted_fruit_counts = sorted(fruit_counts.items(), key=lambda x: x[1][0], reverse=True)
    result = {fruit_type: (count, color) for fruit_type, (count, color) in sorted_fruit_counts}
    return result