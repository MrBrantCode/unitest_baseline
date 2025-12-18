"""
QUESTION:
Implement a function named `advanced_list_manipulate` that takes a list `l` and an integer `n` as input. The function should return a new list where elements at indices not divisible by `n` remain the same as in the original list, but elements at indices divisible by `n` are tripled. The modified elements (tripled or not) should be in reverse order. The function should not modify the original list.
"""

def advanced_list_manipulate(l: list, n: int):
    return sorted([x*3 if i % n == 0 else x for i, x in enumerate(l)], reverse=True)