"""
QUESTION:
Create a function `print_primes` that prints the first `n` prime numbers in reverse order. The function should take two parameters: `n` (the number of prime numbers to print) and an optional `binary` parameter (defaulting to `False`). If `binary` is `True`, the function should print the prime numbers in their binary format, otherwise it should print them in decimal format.
"""

def print_primes(n, binary=False):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    primes.reverse()
    if binary:
        primes = [bin(prime).replace("0b", "") for prime in primes]
    for prime in primes:
        print(prime)