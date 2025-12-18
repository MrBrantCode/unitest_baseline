"""
QUESTION:
Create a function named `hierarchical_dict` that constructs a hierarchical dictionary from two input lists, `l1` and `l2`, where `l1` contains strings and `l2` contains integers. The function should handle repeated values in `l2` and maintain a hierarchical structure. Specifically, if a value in `l1` is repeated, the corresponding values in `l2` should be stored as a list under the same dictionary key. If a value in `l1` is unique, its corresponding value in `l2` should be stored as a single value, not a list.
"""

from collections import defaultdict

def entrance(l1, l2):
    d = defaultdict(list)
    
    for i, j in zip(l1, l2):
        d[i].append(j)

    # Remove lists when it's not necessary
    for key, value in d.items():
        if len(value) == 1:
            d[key] = value[0]

    return dict(d)