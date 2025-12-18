"""
QUESTION:
Create a function `replace_elements` that takes a list `lst` and two elements `old_element` and `new_element` as input. The function should replace all occurrences of `old_element` with `new_element` in the list `lst` and return the modified list. The function must have a time complexity of O(n), where n is the length of the list.
"""

def replace_elements(lst, old_element, new_element):
    for i in range(len(lst)):
        if lst[i] == old_element:
            lst[i] = new_element
    return lst