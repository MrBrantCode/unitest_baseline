"""
QUESTION:
Write a function called "search_prime_numbers" that takes a positive integer "n" as a parameter. The function should find and print all prime numbers up to and including "n". A prime number is a number greater than 1 that is only divisible by 1 and itself. The function must implement the Sieve of Eratosthenes algorithm to generate prime numbers efficiently.

The function should start with a boolean array of size "n+1" to mark numbers as prime or composite. The initial state of the array should be such that all numbers are marked as prime.
"""

def search_prime_numbers(n):
    prime = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n+1) if prime[p]]
    return prime_numbers