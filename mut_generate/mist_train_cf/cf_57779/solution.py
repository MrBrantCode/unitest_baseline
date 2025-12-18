"""
QUESTION:
Design a function called `dict_freq` that calculates the frequency of dictionaries within a given list. The function should produce a dictionary where each dictionary is converted into a string (after being flattened if nested), and the corresponding value of the string signifies the count of its appearances. The function should ignore non-dictionary data types in the input list and be efficient for large inputs.
"""

from collections import defaultdict

def dict_freq(lst):
    def flatten_dict(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    dict_counter = defaultdict(int)
    for item in lst:
        if isinstance(item, dict):
            flattened = flatten_dict(item)
            dict_counter[str(sorted(flattened.items()))] += 1
    return dict_counter