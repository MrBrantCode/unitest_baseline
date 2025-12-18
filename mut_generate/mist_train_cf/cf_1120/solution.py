"""
QUESTION:
Write a function named `shift_list` that takes a list `lst` and an integer `shift` as input, and returns a new list where the elements of `lst` are shifted `shift` positions to the left if `shift` is positive, or to the right if `shift` is negative. The function should handle shift values larger than the length of the list, and return an empty list if `lst` is empty. The function should not modify the original list and should have a time complexity of O(n), where n is the length of the list.
"""

def shift_list(lst, shift):
    if len(lst) == 0:
        return []

    shift = shift % len(lst)
    
    if shift >= 0:
        return lst[shift:] + lst[:shift]
    else:
        return lst[shift:] + lst[:shift]