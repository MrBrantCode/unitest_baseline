"""
QUESTION:
Develop a function `tuples_to_dict_depth` that converts a list of tuples into a dictionary. The list of tuples can have nested tuples with varying levels of nesting. The function should use the first element of each tuple as the key and the last element (regardless of nesting level) as the value in the resulting dictionary.
"""

def tuples_to_dict_depth(tuple_list):
    d = {}
    for tup in tuple_list:
        key = tup[0]
        val = tup[1]
        while isinstance(val, tuple):
            val = val[-1]
        d[key] = val
    return d