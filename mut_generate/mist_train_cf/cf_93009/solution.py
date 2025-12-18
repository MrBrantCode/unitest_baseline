"""
QUESTION:
Write a function `count_fruits` that takes a JSON object containing an array of fruits, each with a type and count, and returns a dictionary where the keys are the types of fruits and the values are the total count of each fruit type, sorted in descending order based on the count. The function should be able to handle any number of fruit types and counts in the input JSON object.
"""

import json

def count_fruits(json_str):
    # Convert the JSON string to a Python object
    data = json.loads(json_str)
    
    # Create a dictionary to store the counts of each fruit type
    fruit_counts = {}
    
    # Iterate over each fruit in the array
    for fruit in data["fruits"]:
        fruit_type = fruit["type"]
        count = fruit["count"]
        
        # If the fruit type is already in the dictionary, add the count to the existing value
        if fruit_type in fruit_counts:
            fruit_counts[fruit_type] += count
        # If the fruit type is not in the dictionary, add a new key-value pair
        else:
            fruit_counts[fruit_type] = count
    
    # Sort the dictionary in descending order based on the count
    sorted_fruit_counts = dict(sorted(fruit_counts.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_fruit_counts