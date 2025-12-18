"""
QUESTION:
Implement a while loop that counts up to 100 and prints only the prime numbers. Define a function `is_prime(n)` to check if a number `n` is prime. The loop should start from 2 and increment by 1 in each iteration. Use the `is_prime(n)` function to check each number and print it if it is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True