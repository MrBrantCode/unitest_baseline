"""
QUESTION:
Write a function `add_and_multiply(a, b)` that takes two integers `a` and `b` as input where 1 <= a, b <= 100. The function should return the sum of `a` and `b`, their product, and a string indicating whether the product is a perfect square or not. If the product is not a perfect square, the function should also return the prime factors of the product in ascending order, separated by commas.
"""

import math

def add_and_multiply(a, b):
    """
    This function calculates the sum and product of two integers.
    It also checks if the product is a perfect square and returns the result.
    If the product is not a perfect square, it returns the prime factors of the product.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing the sum of a and b, their product, 
               a string indicating whether the product is a perfect square or not, 
               and the prime factors of the product if it is not a perfect square.
    """

    sum = a + b
    product = a * b

    if math.sqrt(product).is_integer():
        return sum, product, "Perfect Square", None
    else:
        factors = []
        i = 2
        n = product
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return sum, product, "Not Perfect Square", ",".join(str(f) for f in sorted(factors))