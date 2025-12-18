"""
QUESTION:
Create a Python function `merge_config_defaults(config, defaults)` that takes in two dictionaries, `config` and `defaults`, and returns a new dictionary that recursively merges `config` with `defaults`, prioritizing values from `config` over `defaults`. The function should handle nested dictionaries and support merging lists. If a key exists in both `config` and `defaults`, the value from `config` should be used; if a key exists in `defaults` but not in `config`, the default value should be used.
"""

def merge_config_defaults(config: dict, defaults: dict) -> dict:
    merged = defaults.copy()
    for key, value in config.items():
        if isinstance(value, dict) and key in defaults and isinstance(defaults[key], dict):
            merged[key] = merge_config_defaults(value, defaults[key])
        else:
            merged[key] = value
    return merged