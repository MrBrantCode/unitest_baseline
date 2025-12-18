"""
QUESTION:
Write a function `foo(x, y)` that calculates the product of `x` and `y` using nested loops. The function should take two integers `x` and `y` as input and return an integer as output. The function must use a nested loop structure to calculate the product.
"""

def foo(x, y):
    result = 0
    for i in range(x):
        for j in range(y):
            result += 1
    return result