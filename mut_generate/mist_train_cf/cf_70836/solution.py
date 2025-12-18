"""
QUESTION:
Create a function named `sq_val_odd_key` that takes a nested dictionary as input. The function should return a new nested dictionary where the values of the keys that represent odd integers (either directly or through string representation) are squared, while the values of the keys that represent even integers or non-integer values remain unchanged. The function should handle nested dictionaries recursively and maintain the original structure of the input.
"""

def sq_val_odd_key(d):
    new_dict = {}
    for key, value in d.items():
        try:
            if int(key) % 2 == 1:
                if isinstance(value, dict):
                    value = sq_val_odd_key(value)
                else:
                    value = value*value
            else:
                if isinstance(value, dict):
                    value = sq_val_odd_key(value)
        except (ValueError, TypeError):
            pass
        new_dict[key] = value
    return new_dict