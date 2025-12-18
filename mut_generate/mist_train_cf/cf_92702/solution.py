"""
QUESTION:
Write a function `replace_even_odd(lst)` that takes a list of integers as input and replaces each even number with its square and each odd number with its cube. The function should return the modified list. The list can contain up to 10^6 elements.
"""

def replace_even_odd(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] * lst[i]  # Square even numbers
        else:
            lst[i] = lst[i] * lst[i] * lst[i]  # Cube odd numbers
    return lst