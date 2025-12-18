"""
QUESTION:
Write a function `prime_multiplication_table` that takes an integer `N` as input and prints the multiplication table of the first `N` prime numbers. The function should not take any other inputs.
"""

def prime_multiplication_table(N):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    num = 2

    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1

    for i in primes:
        for j in primes:
            print(i * j, end="\t")
        print()