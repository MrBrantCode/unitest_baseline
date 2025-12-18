"""
QUESTION:
Create a function named `are_dicts_empty` that checks if a dictionary (including any nested dictionaries) is empty and counts the total number of empty dictionaries. The function should handle circular references and other iterable objects such as lists, tuples, and sets. The function should return a tuple where the first element is a boolean indicating whether the dictionary and all its nested dictionaries are empty, and the second element is an integer representing the total number of empty dictionaries.
"""

def are_dicts_empty(d, past_elements=None):
    if past_elements is None:
        past_elements = set()

    is_empty = True
    empty_count = 0

    if id(d) in past_elements:
        return is_empty, empty_count
    past_elements.add(id(d))

    if isinstance(d, dict):
        if not d:
            empty_count += 1
        else:
            is_empty = False
        for value in d.values():
            if isinstance(value, (dict, list, tuple, set)):
                is_nested_empty, nested_counter = are_dicts_empty(value, past_elements)
                is_empty &= is_nested_empty
                empty_count += nested_counter

    if isinstance(d, (list, tuple, set)):
        for i in d:
            if isinstance(i, (dict, list, tuple, set)):
                is_nested_empty, nested_counter = are_dicts_empty(i, past_elements)
                is_empty &= is_nested_empty
                empty_count += nested_counter

    return is_empty, empty_count