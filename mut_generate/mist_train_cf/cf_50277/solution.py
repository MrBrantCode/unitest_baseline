"""
QUESTION:
Create a function `odd_element_reverse` that takes a list `r` and returns a new list where elements at even indices match `r`, while elements at odd indices are in the reverse order of their appearance in `r`. The function should operate on a one-dimensional list and modify it in-place. The input list `r` can contain any type of elements.
"""

def odd_element_reverse(r):
    odd_elements = r[1::2][::-1]
    r[1::2] = odd_elements
    return r