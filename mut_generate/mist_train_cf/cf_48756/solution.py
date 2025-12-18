"""
QUESTION:
Develop a function `find_none_values` that inspects a tuple for None values, yielding the path to each None value as a list of indices and the cumulative count of None values found so far. The function should be able to handle nested tuples and should be optimized for large tuples. If no None value is found, the function should indicate this.
"""

def find_none_values(t, path=None):
    count = 0
    if path is None:
        path = []
    if not isinstance(t, tuple):
        return
    for i, item in enumerate(t):
        new_path = path + [i]
        if item is None:
            count += 1
            yield new_path, count
        elif isinstance(item, tuple):
            for sub_path, sub_count in find_none_values(item, new_path):
                count += sub_count
                yield sub_path, count