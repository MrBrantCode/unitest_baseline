"""
QUESTION:
Design a function named `do_lists_share_common_elements(list1, list2)` that determines if two singly linked data structures share at least one common element. The function should take two lists as arguments and return `True` if a common element is found, and `False` otherwise.
"""

def do_lists_share_common_elements(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False