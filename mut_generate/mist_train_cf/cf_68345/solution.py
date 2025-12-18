"""
QUESTION:
Write a function named `multiply_odd_elements_at_even_indices` that takes a list of numbers `lst` and a multiplier `n` as input. The function should return the product of all odd numbers at even indices in the list, multiplied by `n`. The product should be initialized to 1, and the function should return 0 if the product of the odd numbers at even indices is 0.
"""

def multiply_odd_elements_at_even_indices(lst, n):
    prod = 1

    for idx, el in enumerate(lst):
        if idx % 2 == 0 and el > 0 and el % 2 == 1:
            prod *= el

    return prod * n if prod != 0 else 0