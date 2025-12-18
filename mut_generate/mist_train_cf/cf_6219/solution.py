"""
QUESTION:
Write two functions, `is_element_present` and `find_element_index`, that take a list and an element as input and return a boolean value or the index of the element respectively. The functions should return True or the index only if the element is present in the list and is greater than or equal to the median of the list. If the element is not found or is less than the median, `is_element_present` should return False and `find_element_index` should return -1. The list can contain integers and floats, may have duplicates, and has a maximum length of 10^6 elements. The functions should be efficient for large lists.
"""

def entrance(lst, element):
    sorted_lst = sorted(lst)
    median = sorted_lst[len(sorted_lst) // 2]
    return lst.index(element) if element >= median and element in lst else -1