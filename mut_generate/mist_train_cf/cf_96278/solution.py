"""
QUESTION:
Create two functions, `contains_greater_median(lst, element)` and `index_greater_median(lst, element)`, to search for an integer `element` in a list of integers `lst`. The `contains_greater_median` function should return `True` if `element` is in `lst` and `element` is greater than or equal to the median of `lst`, and `False` otherwise. The `index_greater_median` function should return the index of the first occurrence of `element` in `lst` if `element` is in `lst` and `element` is greater than or equal to the median of `lst`, and -1 otherwise.
"""

def contains_greater_median(lst, element):
    if element in lst and element >= find_median(lst):
        return True
    return False

def index_greater_median(lst, element):
    if element in lst and element >= find_median(lst):
        return lst.index(element)
    return -1

def find_median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2] + sorted_lst[length // 2 - 1]) / 2
    else:
        return sorted_lst[length // 2]