"""
QUESTION:
Write a function that starts a decrementing loop from 100 and stops when it encounters a prime number. Include a separate function named `is_prime(n)` to check if a number is prime. The loop should stop immediately when a prime number is found and should not continue to decrement further.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def entrance():
    i = 100
    while i > 0:
        if is_prime(i):
            return i
        i -= 1