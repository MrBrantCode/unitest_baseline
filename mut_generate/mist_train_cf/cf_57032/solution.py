"""
QUESTION:
Write a function `remove_element(nested_list, target)` that removes all occurrences of `target` in a nested list `nested_list`. The function should work for arbitrary levels of nesting and return the resulting list after removal. Assume that `target` is a string and at least one instance of `target` exists in the list.
"""

def remove_element(nested_list, target):
    result = []
    for i in nested_list:
        if type(i) is list:
            i = remove_element(i, target)
            if i:
                result.append(i)
        elif i != target:
            result.append(i)
    return result