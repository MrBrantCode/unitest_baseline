"""
QUESTION:
Write a function named `multiply_lists` that takes two lists, `list1` and `list2`, as parameters, where `list1` is a list of characters and `list2` is a list of integers. The function should multiply each character in `list1` by the corresponding integer in `list2` and join the result to form a single string. If the lengths of `list1` and `list2` are not equal, the function should return 'The lists do not have the same length.'
"""

def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        return 'The lists do not have the same length.'
    else:
        return ''.join([char*number for char, number in zip(list1, list2)])