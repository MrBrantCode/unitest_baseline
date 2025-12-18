"""
QUESTION:
Implement the function `remove_duplicated_keep_order(value_in_tuple)` that takes a tuple `value_in_tuple` as input and returns a new tuple with duplicate elements removed while maintaining the original order of elements.
"""

def remove_duplicated_keep_order(value_in_tuple):
    new_tuple = []
    for i in value_in_tuple:
        if i not in new_tuple:
            new_tuple.append(i)
    return tuple(new_tuple)