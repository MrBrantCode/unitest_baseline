"""
QUESTION:
Create a function `modify_list(str, lst, n)` that takes a string `str`, a list `lst`, and an integer `n` as parameters. If `str` is in `lst`, perform a cyclic rotation on `lst` `n` times to the right. If `str` is not in `lst`, add `str` to `lst` `n` times. Return the modified list. The cyclic rotation moves the last element of the list to the front.
"""

def entrance(s, lst, n):
    if s in lst:
        # If 's' is present, perform cyclic rotation 'n' times
        for _ in range(n):
            lst = [lst[-1]] + lst[:-1]
    else:
        # If 's' is not present, add it 'n' times
        lst.extend([s] * n)
    return lst