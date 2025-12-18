"""
QUESTION:
Implement the `remove_element_from_tuple` function, which takes a tuple of integers or strings and a target element as input, and returns a new tuple with the specified element removed while maintaining the order of the remaining elements. If the target element is not present in the tuple, the function should return the original tuple unchanged.
"""

def remove_element_from_tuple(tuple_input, target_element):
    new_tuple = ()
    for element in tuple_input:
        if element != target_element:
            new_tuple += (element,)
    return new_tuple