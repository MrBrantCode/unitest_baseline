"""
QUESTION:
Create a function called `product_in_range` that takes a list of integers `l`, a minimum value `min_val`, a maximum value `max_val`, and an additional value `add_val` as parameters. The function should calculate the product of all integers in the list, add `add_val` to the product, and return `True` if the result is within the range `[min_val, max_val]` (inclusive) and `False` otherwise. The time complexity of the function should be less than O(n^2).
"""

def product_in_range(l: list, min_val: int, max_val: int, add_val: int) -> bool:
    result = 1
    for i in l:
        result *= i
    result += add_val
    return min_val <= result <= max_val 