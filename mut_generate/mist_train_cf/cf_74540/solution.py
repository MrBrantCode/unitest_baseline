"""
QUESTION:
Write a function `convert_to_json(hashmap)` that takes a dictionary as input and returns a string representing the dictionary in JSON format. The function should not use any built-in or external JSON libraries. The input dictionary is guaranteed to have string keys and values.
"""

def convert_to_json(hashmap):
    json = "{"
    
    # Iterating through the hashmap
    for key, value in hashmap.items():
        json += "\"" + key + "\": \"" + value + "\", "
    
    # Remove the last comma and space
    json = json[0:-2]
    json += "}"
    
    return json