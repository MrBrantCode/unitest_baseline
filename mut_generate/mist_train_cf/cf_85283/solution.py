"""
QUESTION:
Create a function `sort_dict(d)` that takes a dictionary `d` as input and returns a new dictionary with the same keys, but with the items ordered based on their values. The values can be either numeric (int or float) or strings. The numeric values should be ordered in ascending order, and the string values should be ordered alphabetically. The function should be able to handle a mix of numeric and string values in the dictionary.
"""

def sort_dict(d):
    num_dict = {key: value for key, value in d.items() if isinstance(value, (int, float))}
    str_dict = {key: value for key, value in d.items() if isinstance(value, str)}

    sorted_nums = sorted(num_dict.items(), key=lambda x: x[1])
    sorted_strs = sorted(str_dict.items(), key=lambda x: x[1])

    return dict(sorted_nums + sorted_strs)