"""
QUESTION:
Create a function named `create_dict_check_type` that takes two lists `list_one` and `list_two` and an optional `default_value` parameter. The function should create a dictionary where the keys are elements from `list_one` and the values are elements from `list_two`, with corresponding indices. If one list is longer, fill the shorter list with `default_value` (defaulting to `None`). The function should then check if all dictionary keys are of the same data type and return the dictionary along with a boolean indicating whether the keys are of the same type.
"""

def create_dict_check_type(list_one, list_two, default_value=None):
    if len(list_one) > len(list_two):
        list_two = list_two + [default_value]*(len(list_one)-len(list_two))
    elif len(list_one) < len(list_two):
        list_one = list_one + [default_value]*(len(list_two)-len(list_one))

    result_dict = dict(zip(list_one, list_two))

    types = set(type(key) for key in result_dict.keys())
    return result_dict, len(types) == 1