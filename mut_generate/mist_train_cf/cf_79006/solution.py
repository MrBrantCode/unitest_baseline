"""
QUESTION:
Write a function `flatten_dict` that takes a nested dictionary `d` and returns a flattened dictionary where each key represents the hierarchy of the input dictionaries. The keys in the output dictionary should be produced by joining the keys in the path from the root to the leaf node, separating them with a period ("."). The function should work with dictionaries of varying depth.
"""

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)