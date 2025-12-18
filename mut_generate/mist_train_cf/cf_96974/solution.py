"""
QUESTION:
Write a function named `get_matching_keys` that takes two parameters: `dictionary` and `key_list`. The function should return a new list containing the keys from `dictionary` that are also present in `key_list`, excluding any keys that contain numeric characters. The returned list should be sorted in descending order.
"""

def get_matching_keys(dictionary, key_list):
    matching_keys = []

    for key in key_list:
        if key in dictionary and not any(char.isdigit() for char in key):
            matching_keys.append(key)

    matching_keys.sort(reverse=True)

    return matching_keys