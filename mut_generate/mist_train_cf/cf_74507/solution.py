"""
QUESTION:
Write a function called `squared_primes` that takes an array of integers as input and returns two values: an array of the squared values of only the prime numbers in the input array, and the sum of all the squared prime values in the output array. Implement your own prime-checking function.
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

def squared_primes(arr):
    prime_squares = [n ** 2 for n in arr if is_prime(n)]
    return prime_squares, sum(prime_squares)