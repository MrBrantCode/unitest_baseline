"""
QUESTION:
Implement the function `reverse_list(lst)` that takes a list as input and returns the reversed list. The function should not use any built-in list functions (e.g., `insert`, `append`, `reverse`), additional memory space, or any looping constructs (e.g., `for`, `while`).
"""

def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]