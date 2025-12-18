"""
QUESTION:
Write a function `is_sublist(main_list, sublist)` to determine whether `sublist` is a sublist of `main_list`, handling nested lists and different data types within the lists. The function should return `True` if `sublist` is a sublist of `main_list` and `False` otherwise. The function should be able to handle cases where `sublist` is an empty list, `sublist` is equal to `main_list`, and where the length of `sublist` is greater than the length of `main_list`. The function should also be able to handle cases where `sublist` contains elements that are not lists, in which case it should check if the element is present in `main_list`. Note that the function does not need to handle lists containing dictionaries or other complex data types that cannot be compared directly.
"""

def is_sublist(main_list, sublist):
    if isinstance(sublist, list):
        if sublist == []:
            return True
        elif sublist == main_list:
            return True
        elif len(sublist) > len(main_list):
            return False
        else:
            for i in range(len(main_list)):
                if main_list[i] == sublist[0]:
                    return is_sublist(main_list[i+1:], sublist[1:])
            return False
    else:
        return sublist in main_list