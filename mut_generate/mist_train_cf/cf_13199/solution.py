"""
QUESTION:
Write a function named `replace_even_odd` that takes a list of integers as input, replaces each even number with its square and each odd number with its cube, and returns the modified list. The function should be able to handle lists with up to 10^6 elements.
"""

def replace_even_odd(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] * lst[i]  # Square even numbers
        else:
            lst[i] = lst[i] * lst[i] * lst[i]  # Cube odd numbers
    return lst