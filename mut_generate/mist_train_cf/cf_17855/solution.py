"""
QUESTION:
Implement a function named `remove_element_from_tuple` that takes a tuple of integers or strings and a target element as input, and returns a new tuple with all occurrences of the target element removed while maintaining the order of the remaining elements. The function should not use any built-in functions or libraries, and its time complexity should be O(n) and space complexity should be O(1), where n is the size of the tuple.
"""

def remove_element_from_tuple(tup, element):
    new_tuple = ()
    for item in tup:
        if item != element:
            new_tuple += (item,)
    return new_tuple