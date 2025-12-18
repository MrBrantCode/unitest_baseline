"""
QUESTION:
Construct a function `get_cumulative_sum_complex_dict` that calculates the cumulative sum of all integers in a multi-tiered dictionary. The dictionary may contain other dictionaries, lists, tuples, sets, and other complex data structures as values, with any hashable type as keys. The function should be able to handle circular references, non-integer values, and edge cases without interruption. The function should ignore non-integer values and return the aggregate sum of all integer values found.
"""

def get_cumulative_sum_complex_dict(dict_obj, seen=None):
    if seen is None:
        seen = set()  # used to handle circular references
    if id(dict_obj) in seen:  # check if current object was already iterated over
        return 0
    seen.add(id(dict_obj))  
    cumulative_sum = 0
    if isinstance(dict_obj, dict):
        iter_obj = dict_obj.values()
    elif isinstance(dict_obj, (list, tuple, set)):
        iter_obj = dict_obj
    elif isinstance(dict_obj, int):
        return dict_obj
    else:
        return 0  # ignore non-integer values and other unrecognized types
      
    for item in iter_obj:
        cumulative_sum += get_cumulative_sum_complex_dict(item, seen)
    return cumulative_sum