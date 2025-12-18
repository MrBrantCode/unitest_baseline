"""
QUESTION:
Create a function `get_keys_sorted_by_sum_length` that takes a list of dictionaries as input, where each dictionary has string keys and values that can be converted to strings. The function should return a list of keys in descending order based on the sum of the lengths of their corresponding values across all dictionaries. The function should be able to handle duplicate keys across different dictionaries.
"""

from typing import List

def get_keys_sorted_by_sum_length(my_list: List[dict]) -> List[str]:
    # Create a dictionary to store the sum of lengths for each key
    key_lengths = {}
    
    # Iterate over each dictionary in the input list
    for dictionary in my_list:
        # Iterate over each key-value pair in the current dictionary
        for key, value in dictionary.items():
            # If the key is not already in the dictionary, initialize its length sum as 0
            if key not in key_lengths:
                key_lengths[key] = 0
            # Add the length of the value to the sum for the current key
            key_lengths[key] += len(str(value))
    
    # Sort the keys based on their sum of lengths in descending order
    sorted_keys = sorted(key_lengths.keys(), key=lambda x: key_lengths[x], reverse=True)
    
    return sorted_keys