"""
QUESTION:
Write a function `merge(d1, d2)` that takes two dictionaries `d1` and `d2` as input and returns a new dictionary where shared keys retain data from both dictionaries by appending values into a list instead of replacing them. If the shared keys have different types, the function should handle the merge accordingly, treating lists and non-lists as separate types and recursively merging dictionaries.
"""

def merge(d1, d2):
    for k, v in d2.items():
        if isinstance(v, dict) and k in d1 and isinstance(d1[k], dict):
            merge(d1[k], v)
        elif k in d1 and isinstance(d1[k], dict) and not isinstance(v, dict):
            d1[k] = merge(d1[k], {"": v})
        elif k in d1 and not isinstance(d1[k], dict) and isinstance(v, dict):
            d1[k] = merge({"": d1[k]}, v)
        elif k in d1 and not isinstance(d1[k], list):
            d1[k] = [d1[k], v]
        elif k in d1 and isinstance(d1[k], list):
            d1[k].append(v)
        else:
            d1[k] = v
    return d1