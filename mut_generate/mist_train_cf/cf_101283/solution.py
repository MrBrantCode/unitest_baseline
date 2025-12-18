"""
QUESTION:
Create a recursive function `sum_odd_primes(n)` that calculates the sum of the first `n` odd prime numbers. The function should use another helper function `is_prime(num)` to check if a number is prime. Implement the following restrictions: 
- The function `is_prime(num)` should be able to check if a number is prime.
- The function `sum_odd_primes(n)` should start checking from the first odd prime number, which is 3.
- The function `sum_odd_primes(n)` should return the sum of the first `n` odd prime numbers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def sum_odd_primes(n, i=3, count=0, total=0):
    if count == n:
        return total
    if is_prime(i) and i % 2 == 1:
        total += i
        count += 1
    return sum_odd_primes(n, i+1, count, total)