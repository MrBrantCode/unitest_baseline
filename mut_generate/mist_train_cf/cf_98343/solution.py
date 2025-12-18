"""
QUESTION:
Create a function `complex_formula` that applies the mathematical formula `num ** 2 + 2 * num + 1` to each element in the list `nums = [1, 2, 3, 4, 5]` using the `map()` function and returns the new list of transformed integers. The `complex_formula` function should take an integer as input and return the result of the formula. The new list should be generated without modifying the original list.
"""

def complex_formula(num):
    return num ** 2 + 2 * num + 1