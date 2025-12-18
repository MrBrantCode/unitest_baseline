"""
QUESTION:
Create a function named `check_prime(n)` that checks if a number `n` is prime. Then use this function to generate a list of all prime numbers below 100 using a list comprehension. The function should be efficient by checking for divisibility by 2 separately, only generating odd divisors, and checking for divisors up to the square root of `n`.
"""

def check_prime(n):
    if n == 1:
        return False # 1 is not considered a prime number
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2): 
        if n % d == 0:
            return False
    return True