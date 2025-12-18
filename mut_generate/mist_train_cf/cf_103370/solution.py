"""
QUESTION:
Write a function `delete_key(dictionary, key)` that deletes all occurrences of the given key from the dictionary. The function should have a time complexity of O(n) or better, where n is the number of key-value pairs in the dictionary. The dictionary may contain multiple values with the same key.
"""

def delete_key(dictionary, key):
    # Create a new dictionary to store the updated key-value pairs
    new_dict = {}
    
    # Iterate over each key-value pair in the dictionary
    for k, v in dictionary.items():
        # Check if the key is equal to the given key
        if k != key:
            new_dict[k] = v
    
    return new_dict