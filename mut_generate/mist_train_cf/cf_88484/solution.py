"""
QUESTION:
Create a function called `is_prime()` that takes an integer `num` as input and returns a boolean value indicating whether `num` is a prime number or not. Implement the `is_prime()` function to check for primality by only testing divisibility up to the square root of `num`. 

Restrictions: 
- Do not modify the function name.
- The function should only check divisibility up to the square root of `num`.
- The function should return `False` for numbers less than 2.
- The function should return `True` for prime numbers and `False` otherwise.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True