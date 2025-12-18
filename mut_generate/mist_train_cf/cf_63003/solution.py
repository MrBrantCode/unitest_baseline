"""
QUESTION:
Create a function `product_of_primes(n)` that calculates the product of all prime numbers less than or equal to `n`, and returns the sum of all digits in that product. The input `n` must be a positive integer. If `n` is not a positive integer, the function should return an error message.
"""

import math

def product_of_primes(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input should be a positive integer."

    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num > 2 and num % 2 == 0:
            return False

        max_div = math.floor(math.sqrt(num))
        for i in range(3, 1 + max_div, 2):
            if num % i == 0:
                return False
        return True

    product = 1
    for num in range(2, n+1):
        if is_prime(num):
            product *= num
    
    return sum(int(digit) for digit in str(product))