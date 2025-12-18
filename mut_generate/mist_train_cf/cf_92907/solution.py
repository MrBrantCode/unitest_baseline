"""
QUESTION:
Write a function `sort_dictionary_of_dictionaries(data, key)` to sort a dictionary of dictionaries in descending order based on a given key. The key can be nested within multiple levels of dictionaries and lists. The function should have a time complexity of O(n log n) or better, where n is the total number of elements in the dictionary.

The function should take two parameters: `data`, a dictionary of dictionaries, and `key`, a string representing the key to sort by. If the key is nested, it should be specified using dot notation (e.g., 'friends.age'). 

The function should return a new dictionary with the same structure as the input, but with the dictionaries sorted in descending order based on the given key.
"""

def sort_dictionary_of_dictionaries(data, key):
    def get_nested_value(data, keys):
        if isinstance(data, dict):
            k = keys.pop(0)
            if k in data:
                if isinstance(data[k], dict):
                    return get_nested_value(data[k], keys)
                else:
                    return data[k]
            else:
                return None
        elif isinstance(data, list):
            values = []
            for item in data:
                value = get_nested_value(item, keys.copy())
                if value is not None:
                    values.append(value)
            return values if values else None
        else:
            return None

    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = sort_dictionary_of_dictionaries(v, key)
        return dict(sorted(data.items(), key=lambda x: get_nested_value(x[1], key.split('.')), reverse=True))
    elif isinstance(data, list):
        return sorted(data, key=lambda x: get_nested_value(x, key.split('.')), reverse=True)
    else:
        return data