"""
QUESTION:
Create a function called `find_common_items` that takes two lists `list1` and `list2` as input, both of which can contain integers, floating-point numbers, and strings, and may have a maximum length of 1000. The function should return a list containing all unique common items between `list1` and `list2`, handling any nested lists within the input lists by flattening them and considering their elements as part of the original list.
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
    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items