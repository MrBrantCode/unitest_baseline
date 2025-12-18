"""
QUESTION:
Write a function `replace_element(lst, old_element, new_element)` to replace all occurrences of `old_element` in `lst` with `new_element`. The function should work with both non-nested and nested elements, maintaining the overall structure and order of the original list. The time complexity should be O(n), where n is the length of the list. Assume the input list has at most one level of nesting.
"""

def replace_element(lst, old_element, new_element):
    if lst == old_element:
        return new_element
    if isinstance(lst, list):
        new_lst = []
        for item in lst:
            new_lst.append(replace_element(item, old_element, new_element))
        return new_lst
    else:
        return lst