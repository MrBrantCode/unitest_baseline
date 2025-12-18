"""
QUESTION:
Create a function named `common` that takes three lists as input and returns a sorted list of unique elements common to all three lists without using any built-in Python list functions.
"""

def common(l1: list, l2: list, l3: list):
    """Returns a sorted list of unique elements common to all three lists"""
    def is_in_list(lst, item):
        for i in lst:
            if i == item:
                return True
        return False

    def append_to_list(lst, item):
        if not is_in_list(lst, item):
            lst += [item]
            return True
        return False

    def sort_list(lst):
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst

    common_elements = []
    for i in l1:
        if is_in_list(l2, i) and is_in_list(l3, i):
            append_to_list(common_elements, i)
    return sort_list(common_elements)