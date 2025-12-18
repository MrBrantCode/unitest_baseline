"""
QUESTION:
Write a function called `intersect` that takes two dictionaries `d1` and `d2` as input and returns a new dictionary containing the intersection of `d1` and `d2` based on both keys and values. The function should handle nested dictionaries, considering them intersecting if both the key and the value inside are the same.
"""

def intersect(d1, d2):
    intersected_dict = {}

    for k, v in d1.items():
        if k in d2:
            if isinstance(v, dict):
                nested = intersect(d1[k], d2[k])
                if len(nested.keys()) > 0:
                    intersected_dict[k] = nested
            elif v == d2[k]:
                intersected_dict[k] = v

    return intersected_dict