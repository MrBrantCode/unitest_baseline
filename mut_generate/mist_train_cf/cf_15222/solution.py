"""
QUESTION:
Write a function named `get_keys_with_highest_value` that takes a dictionary `d` as input and returns a list of keys with the highest value. The function should handle dictionaries of any size and have a time complexity of O(n). If multiple keys have the same highest value, all of them should be returned in the list.
"""

def entrance(d):
    max_value = float('-inf')
    max_keys = []
    
    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_keys = [key]
        elif value == max_value:
            max_keys.append(key)
    
    return max_keys