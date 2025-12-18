"""
QUESTION:
Create a function `replace_element` in Python that takes a list `lst`, an element `target`, and a replacement element `replacement` as inputs. The function should replace all occurrences of `target` in `lst` with `replacement`, handling cases where `target` is a nested list or dictionary. The function should maintain the overall structure and order of `lst` and have a time complexity of O(n), where n is the length of `lst`. Assume that `lst` will not have more than one level of nesting for dictionaries.
"""

def replace_element(lst, target, replacement):
    def replace_dict(dct):
        for key in dct:
            if dct[key] == target:
                dct[key] = replacement
            elif isinstance(dct[key], list):
                dct[key] = replace_element(dct[key], target, replacement)
        return dct

    for i in range(len(lst)):
        if lst[i] == target:
            lst[i] = replacement
        elif isinstance(lst[i], list):
            lst[i] = replace_element(lst[i], target, replacement)
        elif isinstance(lst[i], dict):
            lst[i] = replace_dict(lst[i])
    return lst