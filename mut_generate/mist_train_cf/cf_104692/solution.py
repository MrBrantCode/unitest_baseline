"""
QUESTION:
Write two functions, `contains_greater_median(lst, element)` and `index_greater_median(lst, element)`, to check if a given list contains a specific element. The list contains only integers and may have duplicates. The functions should consider the element's presence and its relation to the median of the list.

The `contains_greater_median` function should return `True` if the element is present in the list and is greater than or equal to the median, and `False` otherwise. The `index_greater_median` function should return the index of the first occurrence of the element in the list if it is greater than or equal to the median, and -1 otherwise.
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