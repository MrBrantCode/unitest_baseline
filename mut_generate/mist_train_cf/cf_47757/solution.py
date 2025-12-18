"""
QUESTION:
Create a function `create_dictionary(keys, values)` that takes two lists as input, `keys` and `values`, and returns a dictionary where the elements of `keys` are the keys and the elements of `values` are the values. If the lengths of the lists are different, fill in any missing values with `None` by extending the shorter list.
"""

def create_dictionary(keys, values):
    len_diff = len(keys) - len(values)
    if len_diff > 0:   # if keys are more than values
        values.extend([None] * len_diff)
    elif len_diff < 0:  # if values are more than keys
        keys.extend([None] * abs(len_diff))

    return dict(zip(keys, values))