"""
QUESTION:
Develop a function `delete_odd_index(lst, element)` that takes a list `lst` and an element as input, and returns the modified list with the element removed if it is located at an odd index. If the element is not found in the list or is at an even index, return the original list.
"""

def delete_odd_index(lst, element):
    try:
        index = lst.index(element)
    except ValueError:
        return lst

    if index % 2 != 0:
        del lst[index]

    return lst