"""
QUESTION:
Write a function `traverse_dict` that takes a dictionary `d` as input and returns a dictionary where the keys are the paths from the root to each leaf node in the form of a string (e.g., 'level1.level2a.level3a') and the values are the aggregate of all numerical values within each path string. The function must handle dictionaries of arbitrary size and complexity.
"""

def traverse_dict(d, path=None, out=None):
    if path is None:
        path = []
    if out is None:
        out = {}

    for k, v in d.items():
        new_path = path + [k]
        if isinstance(v, dict):
            traverse_dict(v, new_path, out)
        elif isinstance(v, (int, float)):
            out['.'.join(new_path)] = v

    return out