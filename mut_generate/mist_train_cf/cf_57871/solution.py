"""
QUESTION:
Write a function `flatten_dict(d, parent_key='', sep='_')` that takes a deeply nested dictionary `d` as input and returns a one-level dictionary. The function should recursively flatten the dictionary, using `sep` to separate the keys of the nested dictionaries from their parent keys. If `sep` is not provided, it defaults to an underscore. The function should also handle cases where `d` is not a dictionary or where the values in `d` are not dictionaries or primitive types.
"""

def entance(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(entance(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)