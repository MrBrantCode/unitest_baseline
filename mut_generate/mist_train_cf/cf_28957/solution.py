"""
QUESTION:
Write a function `flatten_dict(d, delimiter='.')` that takes a nested dictionary `d` and an optional delimiter (default is '.') and returns a flattened dictionary where the keys are concatenated with the delimiter to represent the original nested structure. The function should handle arbitrary levels of nesting.
"""

def flatten_dict(d, delimiter='.'):
    """Flattens a nested dictionary.

    Args:
        d: A nested dictionary
        delimiter: A string used to concatenate keys (default is '.')

    Returns:
        dict: A flattened dictionary

    """
    def _flatten_dict_helper(items, parent_key='', sep=delimiter):
        flattened_dict = {}
        for k, v in items.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                flattened_dict.update(_flatten_dict_helper(v, new_key, sep))
            else:
                flattened_dict[new_key] = v
        return flattened_dict

    return _flatten_dict_helper(d)