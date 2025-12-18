"""
QUESTION:
Implement a function `sort_json_keys(json_obj)` that takes a JSON object as input, sorts its keys in descending order based on the following criteria:
- length of the key
- alphabetical order
- number of vowels in the key
- number of consonants in the key
- sum of ASCII values of all characters in the key

The function should return a dictionary with the sorted keys and their respective values.
"""

import json

def sort_json_keys(json_obj):
    # Parse the input JSON object
    data = json.loads(json_obj)
    
    # Define the custom sorting function
    def sort_key(key):
        # Calculate the length of the key
        length = len(key)
        
        # Calculate the number of vowels and consonants in the key
        vowels = sum(1 for char in key.lower() if char in 'aeiou')
        consonants = sum(1 for char in key.lower() if char.isalpha() and char not in 'aeiou')
        
        # Calculate the sum of ASCII values of all characters in the key
        ascii_sum = sum(ord(char) for char in key)
        
        # Return a tuple of sort criteria
        return (-length, key, -vowels, -consonants, -ascii_sum)
    
    # Sort the keys of the dictionary using the custom sorting function
    sorted_keys = sorted(data.keys(), key=sort_key)
    
    # Create a new dictionary with the sorted keys and their respective values
    sorted_dict = {key: data[key] for key in sorted_keys}
    
    # Return the sorted dictionary
    return sorted_dict