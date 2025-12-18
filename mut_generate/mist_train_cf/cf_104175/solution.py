"""
QUESTION:
Implement a function named `store_key_value` that takes a dictionary, a string key, and a positive integer value as input. The key must be a string containing only alphabetic characters. If the key already exists in the dictionary, update its value and increment the count of updates. If not, add the key-value pair and initialize the update count to 1. The update count should be stored in the dictionary with a key in the format "key_updates".
"""

def store_key_value(dictionary, key, value):
    # Check if key is a string containing only alphabetic characters
    if not key.isalpha():
        print("Invalid key! The key must be a string containing only alphabetic characters.")
        return

    # Check if value is a positive integer
    if not isinstance(value, int) or value <= 0:
        print("Invalid value! The value must be a positive integer.")
        return

    # Check if the key already exists in the dictionary
    if key in dictionary:
        dictionary[key] = value
        dictionary[key+"_updates"] = dictionary.get(key+"_updates", 0) + 1
    else:
        dictionary[key] = value
        dictionary[key+"_updates"] = 1