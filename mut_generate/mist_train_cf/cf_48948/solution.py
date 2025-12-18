"""
QUESTION:
Create a function named `add_prefix_to_list_elements` that accepts three parameters: a string `prefix`, a multi-level nested list `my_list`, and an integer `depth`. The function should recursively traverse the nested list up to `depth` levels and return a new nested list with each constituent element (up to the `depth`-th level) initiated by the given `prefix`. The function should also handle cases where `depth` exceeds the actual depth of the nested list.
"""

def add_prefix_to_list_elements(prefix, my_list, depth, current_depth=0):
    if not isinstance(my_list, list) or current_depth == depth:
        return my_list

    new_list = []
    for element in my_list:
        if isinstance(element, list):
            new_list.append(
                add_prefix_to_list_elements(prefix, element, depth, current_depth + 1)
            )
        else:
            new_list.append(f"{prefix}{element}")

    return new_list