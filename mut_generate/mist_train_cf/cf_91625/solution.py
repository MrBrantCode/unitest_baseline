"""
QUESTION:
Implement a function `remove_element_from_tuple` that takes a tuple and a target element as input, and returns a new tuple with the target element removed. The order of the remaining elements in the tuple should be maintained, and if the target element is not present in the tuple, the function should return the original tuple unchanged.
"""

def remove_element_from_tuple(tuple_input, target_element):
    new_tuple = ()
    for element in tuple_input:
        if element != target_element:
            new_tuple += (element,)
    return new_tuple