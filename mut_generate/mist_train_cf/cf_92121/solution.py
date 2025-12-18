"""
QUESTION:
Create a function named `print_primes_desc` that takes an array of integers as input and prints all the prime numbers in the array in descending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_desc(arr):
    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    for prime in primes:
        print(prime)