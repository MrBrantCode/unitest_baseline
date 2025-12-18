"""
QUESTION:
Write a function named `is_sublist` that checks whether a given list (potential_sublist) is a sublist of another list (main_list). The function should be able to handle nested lists and different data types within the lists. It should return True if all elements of the potential_sublist are present in the main_list and False otherwise.
"""

from collections.abc import Iterable

def is_sublist(main_list, potential_sublist):
    def is_sublist_nested(main_list, potential_sublist):
        for i in potential_sublist:
            if isinstance(i, list):
                if not is_sublist_nested(main_list, i):
                    return False
            elif i not in main_list:
                return False
        return True

    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else:
                yield item

    return is_sublist_nested(list(flatten(main_list)), potential_sublist)