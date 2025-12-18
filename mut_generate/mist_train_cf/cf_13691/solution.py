"""
QUESTION:
Write a function `sort_dictionary_of_dictionaries` to sort a dictionary of dictionaries in descending order based on a given key. The key can be a string representing a single key or a dot notation string representing a nested key within multiple levels of dictionaries and lists (e.g., 'friends.age'). The function should have a time complexity of O(n log n) or better, where n is the total number of elements in the dictionary.
"""

def sort_dictionary_of_dictionaries(data, key):
    # Recursive function to get the value associated with a given key
    def get_nested_value(data, keys):
        if isinstance(data, dict):
            key = keys.pop(0)
            if key in data:
                if isinstance(data[key], dict):
                    return get_nested_value(data[key], keys)
                else:
                    return data[key]
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

    # Recursive function to sort the dictionary of dictionaries
    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = sort_dictionary_of_dictionaries(v, key)
        return dict(sorted(data.items(), key=lambda x: get_nested_value(x[1], key.split('.')), reverse=True))
    elif isinstance(data, list):
        return sorted(data, key=lambda x: get_nested_value(x, key.split('.')), reverse=True)
    else:
        return data