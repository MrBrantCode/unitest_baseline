"""
QUESTION:
Write a function `parse_json` that takes a JSON string as input, filters out key-value pairs with values less than 2, prints the remaining pairs in reverse alphabetical order, and returns the count of pairs with values greater than 3.
"""

import json

def parse_json(json_str):
    # Parse the JSON string
    data = json.loads(json_str)

    # Filter and sort the key-value pairs
    filtered_pairs = [(key, value) for key, value in data.items() if isinstance(value, int) and value >= 2]
    filtered_pairs.sort(key=lambda x: x[0], reverse=True)

    # Print the key-value pairs in reverse alphabetical order
    for key, value in filtered_pairs:
        print(key, ":", value)

    # Count the number of pairs with a value greater than 3
    count = sum(1 for value in data.values() if isinstance(value, int) and value > 3)
    return count