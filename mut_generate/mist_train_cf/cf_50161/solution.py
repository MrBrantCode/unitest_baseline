"""
QUESTION:
Create a function `obliterate_tuples` that takes two parameters: `original_tuple` and `tuple_to_remove`. The function should remove all occurrences of `tuple_to_remove` from `original_tuple`, including nested occurrences, while preserving the order of the remaining elements. The function should return the modified tuple. Note that the original tuple is immutable and will not be directly modified; instead, a new tuple will be created with the specified tuples removed.
"""

def obliterate_tuples(original_tuple, tuple_to_remove):
    result = []
    for item in original_tuple:
        if item == tuple_to_remove:
            continue
        elif isinstance(item, tuple):
            result.append(obliterate_tuples(item, tuple_to_remove))
        else:
            result.append(item)
    return tuple(result)