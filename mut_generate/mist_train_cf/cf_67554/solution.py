"""
QUESTION:
Create a function called `complex_flatten` that takes one argument, a potentially nested list, and returns a new list with all sublists flattened into a single level. The function should handle different data types within the list without changing their order and return the elements as is. If the input is not a list, the function should return a message stating the data type of the input. If the list contains non-list data structures like dictionaries or sets, consider them as single elements of the list and do not attempt to flatten them.
"""

def complex_flatten(nested_list):
    if not isinstance(nested_list, list):
        return('Input is not a list, but a {}'.format(type(nested_list)))

    result = []

    for i in nested_list:
        if isinstance(i, list):
            result.extend(complex_flatten(i))
        else:
            result.append(i)
    return result