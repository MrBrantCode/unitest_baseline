"""
QUESTION:
Create a function called `modify_nested_list` that takes a list as input and returns a new list with twice the length of the original. Within each sublist, the order of elements should be reversed, and any duplicates should be removed. Non-list items in the original list should remain unchanged.
"""

def modify_nested_list(original_list):
    new_list = []
    for item in original_list:
        if isinstance(item, list):
            new_sublist = list(set(item))
            new_sublist.reverse()
            new_list.append(new_sublist)
        else:
            new_list.append(item)
    new_list *= 2
    return new_list