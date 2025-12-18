"""
QUESTION:
Write a function `compare_dicts(a, b)` that compares two dictionaries `a` and `b` for equality. The function should ignore the order of key-value pairs and any keys that start with an underscore (_). The dictionaries can contain nested dictionaries as values, and all dictionary values are positive integers. The function should be able to handle dictionaries with up to 1000 key-value pairs.
"""

def compare_dicts(a, b):
    # Check if the dictionaries have the same number of key-value pairs
    if len(a) != len(b):
        return False

    # Ignore keys starting with an underscore
    keys_a = [k for k in a.keys() if not k.startswith('_')]
    keys_b = [k for k in b.keys() if not k.startswith('_')]

    # Check if the dictionaries have the same keys
    if sorted(keys_a) != sorted(keys_b):
        return False

    # Recursively compare the values
    for key in keys_a:
        value_a = a[key]
        value_b = b[key]

        # If both values are dictionaries, recursively compare them
        if isinstance(value_a, dict) and isinstance(value_b, dict):
            if not compare_dicts(value_a, value_b):
                return False
        # If the values are not dictionaries, compare them directly
        elif value_a != value_b:
            return False

    # All key-value pairs are equal
    return True