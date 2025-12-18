"""
QUESTION:
Implement a function `flatten_dict(nested_dict)` that takes a nested dictionary as input and returns a flattened dictionary where the keys are formed by concatenating the nested keys with a dot ('.') separator. The function should handle nested dictionaries of arbitrary depth.
"""

def flatten_dict(nested_dict):
    def flatten_helper(nested_dict, parent_key='', sep='.'):
        items = []
        for k, v in nested_dict.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_helper(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return flatten_helper(nested_dict)