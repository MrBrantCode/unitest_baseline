"""
QUESTION:
Write a function named `print_twin_primes` that prints all twin primes between two input numbers `start` and `end`, where a twin prime is defined as a prime number that is either 2 less or 2 more than another prime number. The function should take `start` and `end` as parameters, find all twin primes within the range `[start, end]`, and print them.
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

def print_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end + 1):
        if is_prime(num) and (is_prime(num - 2) or is_prime(num + 2)):
            twin_primes.append(num)
    print("Twin primes between", start, "and", end, "are:")
    for prime in twin_primes:
        print(prime, "and", prime + 2 if is_prime(prime + 2) else prime - 2)