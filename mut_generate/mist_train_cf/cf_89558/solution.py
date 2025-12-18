"""
QUESTION:
Create a function `replace_element` that takes three parameters: `lst` (the input list), `target` (the element to be replaced), and `replacement` (the element to replace with). The function should replace all occurrences of `target` in `lst` with `replacement`. The function should handle nested lists and dictionaries up to one level of nesting and have a time complexity of O(n), where n is the length of the list.
"""

def replace_element(lst, target, replacement):
    def replace_dict(dct, target, replacement):
        for key in dct:
            if dct[key] == target:
                dct[key] = replacement
            elif isinstance(dct[key], list):
                dct[key] = replace_element(dct[key], target, replacement)
            elif isinstance(dct[key], dict):
                dct[key] = replace_dict(dct[key], target, replacement)
        return dct

    for i in range(len(lst)):
        if lst[i] == target:
            lst[i] = replacement
        elif isinstance(lst[i], list):
            lst[i] = replace_element(lst[i], target, replacement)
        elif isinstance(lst[i], dict):
            lst[i] = replace_dict(lst[i], target, replacement)
    return lst