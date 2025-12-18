"""
QUESTION:
Create a function `search_key_value_pair` that takes two parameters: a search key and a nested object. The function should search for the key-value pair where the key is a string and the value is a dictionary, and all values within the dictionary are positive integers. The function should return the key-value pair if found, or None if not found. The time complexity of the algorithm should be O(n), where n is the number of key-value pairs in the object.
"""

def search_key_value_pair(search_key, obj):
    for key, value in obj.items():
        if key == search_key and isinstance(value, dict) and all(isinstance(val, int) and val > 0 for val in value.values()):
            return {key: value}
    return None