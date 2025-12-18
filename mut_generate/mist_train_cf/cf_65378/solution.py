"""
QUESTION:
Create a function `optimized_prime_factor(n)` that takes an integer `n` as input, where the absolute value of `n` is greater than 1 and `n` is not a prime number. The function should return the largest prime factor of `n`, handling both positive and negative values of `n` efficiently by only checking odd divisors after removing all factors of 2.
"""

def optimized_prime_factor(n: int):
    # Take absolute value for negative inputs
    n = abs(n)
    
    # Handle edge cases
    assert n > 1, "The input number must be greater than 1"
    
    # Divide by 2 as long as possible
    while n % 2 == 0:
        n /= 2
    if n == 1:
        return 2
    
    # If no further division is possible, initialize divisor to 3
    divisor = 3

    while divisor * divisor <= n:
        if n % divisor:
            divisor += 2
        else:
            n /= divisor
    return int(n if n > 1 else divisor)