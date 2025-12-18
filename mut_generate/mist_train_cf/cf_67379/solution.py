"""
QUESTION:
Create a function `is_prime(n)` that checks whether a number `n` is prime. Then use this function to generate a list of 20 distinct prime numbers between 100 and 200. The list should be generated within the range (100, 200) and should not include any duplicates.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True