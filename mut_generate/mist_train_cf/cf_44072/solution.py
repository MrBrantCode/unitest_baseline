"""
QUESTION:
Implement a function named `sort_dict` that takes a dictionary as input where the keys are strings and the values are either integers or dictionaries. The function should sort the outer dictionary based on its values in ascending order. If a value is a dictionary, it should be sorted first and then the smallest value from that dictionary should be used for comparison when sorting the outer dictionary. The function should handle nested dictionaries of any depth.
"""

from collections import OrderedDict

def sort_dict(d):
    for key in d:
        if isinstance(d[key], dict):
            d[key] = sort_dict(d[key])
    return OrderedDict(sorted(d.items(), key=lambda x: min(x[1].values()) if isinstance(x[1],dict) else x[1]))