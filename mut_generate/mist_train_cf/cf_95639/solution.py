"""
QUESTION:
Write a function named `get_keys_sorted_by_value_length` that takes a list of dictionaries as input and returns a list of keys in descending order based on the average length of their corresponding values across all dictionaries. Each dictionary in the input list represents a record where the keys are attributes and the values are corresponding values for each attribute.
"""

from typing import List

def get_keys_sorted_by_value_length(my_list: List[dict]) -> List[str]:
    keys = set()
    values_lengths = {}
    
    # Iterate through each dictionary in the list
    for record in my_list:
        # Iterate through each key-value pair in the dictionary
        for key, value in record.items():
            keys.add(key)  # Add the key to the set of keys
            
            # Update the length of the value for the key
            if key in values_lengths:
                values_lengths[key].append(len(str(value)))
            else:
                values_lengths[key] = [len(str(value))]
    
    # Sort the keys based on the average length of their corresponding values
    sorted_keys = sorted(keys, key=lambda k: sum(values_lengths[k]) / len(values_lengths[k]), reverse=True)
    
    return sorted_keys