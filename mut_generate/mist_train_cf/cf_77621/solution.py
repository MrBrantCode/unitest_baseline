"""
QUESTION:
Implement a function `rotate_left(lst, n)` that takes a list `lst` and an integer `n` as input, and returns a new list that is a rotation of `lst` shifted `n` positions to the left if `n` is positive, or `n` positions to the right if `n` is negative. If `n` is greater than the length of `lst`, it should only rotate the list by the remainder of `n` divided by the length of `lst`. The function should also handle the case where `lst` is empty.
"""

def rotate_left(lst, n):
    if len(lst) == 0:
        return lst
    else:
        n = n % len(lst) 
        return lst[n:] + lst[:n]