"""
QUESTION:
Write a function `get_keys_sorted_by_value_length` that takes in a list of dictionaries as input, where each dictionary represents a record with string keys and values of any type. The function should return a list of keys in descending order based on the average length of their corresponding values across all dictionaries.
"""

from typing import List, Dict

def get_keys_sorted_by_value_length(my_list: List[Dict]) -> List[str]:
    keys = set()
    values_lengths = {}
    
    for record in my_list:
        for key, value in record.items():
            keys.add(key)  
            if key in values_lengths:
                values_lengths[key].append(len(str(value)))
            else:
                values_lengths[key] = [len(str(value))]
    
    sorted_keys = sorted(keys, key=lambda k: sum(values_lengths[k]) / len(values_lengths[k]), reverse=True)
    
    return sorted_keys