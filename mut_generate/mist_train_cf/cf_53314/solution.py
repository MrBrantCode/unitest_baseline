"""
QUESTION:
Create a function named `unique_elements` that takes in a list of dictionaries `hmaps` and a string `key` as input. The function should return a list of unique elements corresponding to the given `key`. The `key` can be a nested key separated by '.'. The function should raise a custom exception if the `key` is not found in any dictionary. The function should be efficient for large inputs.
"""

class KeyNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


def unique_elements(hmaps, key):
    def get_key_elements(hmap, key):
        keys = key.split('.')
        value = hmap
        for each_key in keys:
            if each_key not in value:
                raise KeyNotFoundException('The key was not found in the map')
            value = value[each_key]
        return value

    result_set = set()
    for hmap in hmaps:
        result_value = get_key_elements(hmap, key)
        result_set.add(result_value)
    return list(result_set)