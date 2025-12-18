"""
QUESTION:
Create a function named `first_n_primes` to generate an array of the first 'n' prime numbers, where 'n' is the input parameter, and each prime number must be greater than a specified minimum value, which is also an input parameter. The function should return an array of prime numbers. The array should be in ascending order.
"""

def first_n_primes(n, min_value):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = min_value + (1 - min_value % 2)
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 2
    return primes