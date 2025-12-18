"""
QUESTION:
Create a function `triple_elements` that takes a multidimensional list as input, triples each element in the list while maintaining the original structure, and returns the new list. The function should handle nested lists and non-iterable data types.
"""

def triple_elements(original_list):
    new_list = []
    for i in original_list:
        if isinstance(i, list):
            new_list.append(triple_elements(i))
        else:
            for _ in range(3):
                new_list.append(i)
    return new_list