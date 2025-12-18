"""
QUESTION:
Apply the function `complex_formula` to each element in the list `nums` using the `map()` function. The `complex_formula` is a function that takes in a single integer as an argument and applies the mathematical formula `num ** 2 + 2 * num + 1` to it. The `nums` list is `[1, 2, 3, 4, 5]`. Write a Python function that uses `map()` to generate a new list `new_nums` that consists of the output of the `complex_formula` applied to each element in `nums`.
"""

def complex_formula(num):
    return num ** 2 + 2 * num + 1