"""
QUESTION:
Construct a function `find_primes` that takes an upper limit `n` as input and outputs a list of prime numbers between 2 and `n`. The function should only use a maximum of 3 variables and cannot use any built-in functions or libraries related to prime numbers.
"""

def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes