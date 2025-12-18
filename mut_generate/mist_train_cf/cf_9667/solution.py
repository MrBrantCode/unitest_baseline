"""
QUESTION:
Write a function `shift_list(lst, shift)` that takes a list `lst` and an integer `shift` as input, and returns a new list where the elements of `lst` are shifted `shift` positions to the left if `shift` is positive, and to the right if `shift` is negative. If `shift` is 0 or a multiple of the length of `lst`, return a copy of `lst`. The function should handle shift values larger than the length of `lst` by effectively rotating the list, and should not modify the original list.
"""

def shift_list(lst, shift):
    n = len(lst)
    shift = shift % n
    if shift == 0:
        return lst.copy()
    elif shift > 0:
        return lst[shift:] + lst[:shift]
    else:
        return lst[n+shift:] + lst[:n+shift]