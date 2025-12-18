"""
QUESTION:
Implement a function `sum_product_even(numbers, p=2)` that takes a list of integers `numbers` and an optional parameter `p` with a default value of 2. The function should return a tuple containing the sum and product of even integers in the list that are not divisible by `p`, where `p` is considered only if it is a unique prime number. If no such numbers exist, the function should return a sum of 0 and a product of 1.
"""

from typing import List, Tuple
from functools import reduce

def sum_product_even(numbers: List[int], p: int = 2) -> Tuple[int, int]:
    # Filter out numbers that are even and not divisible by p
    is_unique_prime = lambda x : all([(x%j) for j in range(2, int(x**0.5) + 1)]) and x>1
    def condition(x):
        return x%2 == 0 and ((x % p != 0) if is_unique_prime(p) else True)
    numbers = list(filter(condition, numbers))
    # Compute sum and product
    sum = 0 if not numbers else reduce(lambda x, y: x + y, numbers)
    product = 1 if not numbers else reduce(lambda x, y: x * y, numbers)
    return (sum, product)