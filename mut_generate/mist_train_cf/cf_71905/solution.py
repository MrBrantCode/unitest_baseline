"""
QUESTION:
Write a function `flatten_dict` that takes a dictionary `dd`, a string `separator`, and a string `prefix` as parameters and returns a flattened version of the dictionary. The function should recursively flatten nested dictionaries by concatenating keys using the specified separator. The `separator` defaults to '_' and the `prefix` defaults to an empty string.
"""

def flatten_dict(dd, separator='_', prefix=''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }