"""
QUESTION:
Create a function named `find_common_items` that takes two lists, `list1` and `list2`, as inputs and returns a list of common items between them. The function should ignore any duplicate common items in the resulting list. The input lists can have a maximum length of 1000, may contain positive and negative integers, floating-point numbers, and strings, and may include nested lists. If a nested list is encountered, the function should flatten it and consider its elements as part of the original list.
"""

def find_common_items(list1, list2):
    def flatten_list(lst):
        flattened_list = []
        for item in lst:
            if isinstance(item, list):
                flattened_list.extend(flatten_list(item))
            else:
                flattened_list.append(item)
        return flattened_list

    list1 = flatten_list(list1)
    list2 = flatten_list(list2)

    common_items = set(list1) & set(list2)
    return list(common_items)