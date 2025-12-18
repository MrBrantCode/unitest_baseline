"""
QUESTION:
Write a function that prints the first 100 prime numbers in reverse order.
"""

def print_first_n_primes_in_reverse(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    for prime in reversed(primes):
        print(prime)