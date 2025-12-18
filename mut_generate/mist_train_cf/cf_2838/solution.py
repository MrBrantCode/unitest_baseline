"""
QUESTION:
Write a function named `sum_primes` that calculates the sum of all prime numbers from 1 to 1000, excluding 2 and 3. The function should return this sum. The function should not take any arguments.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes():
    sum_primes = 0
    for num in range(1, 1001):
        if num != 2 and num != 3 and is_prime(num):
            sum_primes += num
    return sum_primes