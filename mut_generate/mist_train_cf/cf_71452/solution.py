"""
QUESTION:
Create a function called `even_product` that calculates the product of all even numbers from 2 to a given integer `n`. The function should take `n` as input, where `n` is an integer greater than or equal to 2, and return the product of all even numbers in the range 2 to `n` (inclusive).
"""

def even_product(n):
    product = 1
    for i in range(2,n+1):
        if i % 2 == 0:
            product *= i
    return product