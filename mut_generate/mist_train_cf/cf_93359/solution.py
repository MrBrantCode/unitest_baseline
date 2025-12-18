"""
QUESTION:
Create a function named `modify_nested_list` that takes a nested list as an argument and returns a new list with the following properties: 
- The new list has twice the length of the original list.
- The order of elements in each sublist is reversed.
- There are no duplicate elements within each sublist.
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