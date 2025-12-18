"""
QUESTION:
Design a function `operate_on_dicts` that takes in three dictionaries: `dict1` and `dict2` with string keys and integer values, and `operations_dict` with operation names as keys and a boolean status as values. The function performs the operations in `operations_dict` on `dict1` and `dict2` in the order they appear, and returns the result dictionary. The operations can be "merge", "common_keys", "unique_keys", or "sort_by_value". If an operation cannot be performed, the function returns an error message. The results are in ascending order of keys.
"""

def operate_on_dicts(dict1, dict2, operations_dict):
    """
    Performs operations on two dictionaries based on the operations provided.

    Args:
    dict1 (dict): The first dictionary with string keys and integer values.
    dict2 (dict): The second dictionary with string keys and integer values.
    operations_dict (dict): A dictionary with operation names as keys and a boolean status as values.

    Returns:
    dict: The result dictionary after performing all operations.
    """
    result = {}
    
    # Sort operations by keys
    for operation, status in sorted(operations_dict.items()):
        if status:
            if operation == "merge":
                # Merge dict1 and dict2 into result
                result = {**dict1, **dict2}
            elif operation == "common_keys":
                # Find common keys between dict1 and dict2
                common_keys = dict1.keys() & dict2.keys()
                result = {key: dict1[key] for key in common_keys}
            elif operation == "unique_keys":
                # Find unique keys in each of dict1 and dict2
                unique_keys = (dict1.keys() - dict2.keys()) | (dict2.keys() - dict1.keys())
                if len(unique_keys) == 0:
                    return "Both dictionaries are identical, no unique keys found."
                result = {key: dict1.get(key, dict2.get(key)) for key in unique_keys}
            elif operation == "sort_by_value":
                # Sort result by value
                result = dict(sorted(result.items(), key=lambda item: item[1]))
            else:
                return "Invalid operation."
    
    return result