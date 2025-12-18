"""
QUESTION:
Create a function `is_prime(num)` that checks if a number is prime or not, and another function `generate_prime(n)` that generates the first `n` prime numbers in reverse order using recursive functions and dynamic programming concepts, with a limit of `n` being a positive integer. The `is_prime(num)` function should utilize memoization to optimize performance by storing the 'primeness' of each number in a cache to avoid recomputing it.
"""

cache = {0: False, 1: False} 

def is_prime(num):
    if num in cache:
        return cache[num]

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            cache[num] = False
            return False
    cache[num] = True
    return True

def generate_prime(n):
    prime_numbers = []
    for num in range(2, n**2 + 1):
        if is_prime(num):
            prime_numbers.append(num)
        if len(prime_numbers) == n:
            break
    return prime_numbers[::-1] # return the prime numbers in reverse order