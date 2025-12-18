"""
QUESTION:
Create a function named `remove_element_from_tuple` that takes a tuple and a target element as input, and returns a new tuple with all occurrences of the target element removed. The function must maintain the original order of the remaining elements, handle cases where the target element is not present in the tuple, have a time complexity of O(n), and a space complexity of O(n).
"""

def remove_element_from_tuple(tup, element):
    new_tuple = ()
    for item in tup:
        if item != element:
            new_tuple += (item,)
    return new_tuple