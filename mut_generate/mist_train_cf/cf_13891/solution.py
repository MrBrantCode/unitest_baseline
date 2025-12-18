"""
QUESTION:
Write a function named `count_fruits` that takes a JSON string representing an object with a "fruits" array, where each fruit has a "type" and a "count". The function should return a dictionary where the keys are the types of fruits and the values are the total count of each fruit type, sorted in descending order based on the count.
"""

import json

def count_fruits(json_str):
    data = json.loads(json_str)
    fruit_counts = {}
    
    for fruit in data["fruits"]:
        fruit_type = fruit["type"]
        count = fruit["count"]
        
        if fruit_type in fruit_counts:
            fruit_counts[fruit_type] += count
        else:
            fruit_counts[fruit_type] = count
    
    sorted_fruit_counts = dict(sorted(fruit_counts.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_fruit_counts