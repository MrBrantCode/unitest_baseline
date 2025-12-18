"""
QUESTION:
Create a function `cycpattern_check(a, b)` that checks if string `b` is a subsequence of string `a` (ignoring case sensitivity and special characters) or if `b` is a rotational sequence of a subsequence of `a`. The function should return `True` if `b` meets either condition, and `False` otherwise.
"""

def cycpattern_check(a, b):
    a = "".join(c.lower() for c in a if c.isalnum())
    b = "".join(c.lower() for c in b if c.isalnum())
    a_set = set(a)
    a_temp = "".join(i for i in a if i in b)
    a_list = [i for i in a if i in b]
    b_list = list(b)
    if a_temp != b and all(i in a_set for i in b) and a_temp == "".join(b_list[i] for i in range(len(b_list)) if i in [a_list.index(j) for j in b_list]):
        return True
    dbl_a = a + a
    return b in dbl_a