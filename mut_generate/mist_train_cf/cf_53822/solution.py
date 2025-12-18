"""
QUESTION:
Write a function `cycpattern_check(a, b)` that checks two conditions for two input strings `a` and `b` containing only alphabetical characters. First, it checks if `b` or any rotation of `b` exists as a substring of `a`. Second, it checks if `b` can become a substring of `a` through a series of adjacent letter swaps. The function returns `True` if either condition is met, and `False` otherwise.
"""

def cycpattern_check(a, b):
    # Check if both words contain only alphabetical characters
    if not a.isalpha() or not b.isalpha():
        return False

    # Check if b or its rotation exists in a
    for i in range(len(b)):
        if b in a or b[i:] + b[:i] in a:
            return True

    # Check if b can become a substring of a through a series of adjacent letter swaps
    a_list = list(a)
    a_list.sort()
    b_list = list(b)
    b_list.sort()
    b = "".join(b_list)
    for i in range(len(a) - len(b) + 1):
        a_sub_list = a_list[i : i + len(b)]
        a_sub_list.sort()
        a_sub = "".join(a_sub_list)
        if a_sub == b:
            return True

    return False