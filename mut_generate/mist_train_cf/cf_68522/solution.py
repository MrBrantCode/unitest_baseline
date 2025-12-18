"""
QUESTION:
Design a function named `dict_operations` that takes in three dictionaries: `dict1`, `dict2`, and `operations`. Both `dict1` and `dict2` have string keys and integer values, while `operations` is a dictionary containing a set of operations as strings. The function should perform the operations in the order they appear in `operations` and output the result in ascending order of keys. The operations can be "merge", "common_keys", "unique_keys", "sort_by_value", "sort_by_key", "value_difference", or "key_intersection". If an operation cannot be performed, the function should return an error message. The function should be able to handle large dictionaries with up to 10^6 entries and optimize for time complexity.
"""

def dict_operations(dict1, dict2, operations):
    result = {}

    for operation in operations:
        if operation == 'merge':
            result = {**dict1, **dict2}
        elif operation == 'common_keys':
            result = {k: dict1[k] for k in dict1 if k in dict2}
        elif operation == 'unique_keys':
            if dict1 == dict2:
                return "Error: Dictionaries are identical, no unique keys."

            result = {k: dict1[k] for k in dict1 if k not in dict2}
            result.update({k: dict2[k] for k in dict2 if k not in dict1})
        elif operation == 'sort_by_value':
            result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
        elif operation == 'sort_by_key':
            result = {k: v for k, v in sorted(result.items(), key=lambda item: item[0])}
        elif operation == 'value_difference':
            result = {k: abs(dict1.get(k, 0) - dict2.get(k, 0)) for k in set(dict1) | set(dict2)}
        elif operation == 'key_intersection':
            result = {k: dict1[k] for k in set(dict1) & set(dict2)}
        else:
            return "Error: Invalid operation."

    # Sort by keys before returning
    return {k: v for k, v in sorted(result.items(), key=lambda item: item[0])}