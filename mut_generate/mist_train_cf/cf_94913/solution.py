"""
QUESTION:
Write a recursive function named `multiply_recursive` that takes two positive integers `x` and `y` as input and returns their product without using loops or the multiplication operator. The function should handle the base case where `x` or `y` is zero, and the recursive case where `y` is decremented until it reaches zero.
"""

def multiply_recursive(x, y):
    # Base case: If either x or y is zero, return zero
    if x == 0 or y == 0:
        return 0

    # Recursive case: Multiply x by (y - 1) and add x to the result
    return x + multiply_recursive(x, y - 1)