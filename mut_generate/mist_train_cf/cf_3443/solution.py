"""
QUESTION:
Implement the Sieve of Eratosthenes algorithm in a function named `sieve_of_eratosthenes(start, end)` to generate a sequence of prime numbers between a given range `start` and `end`. Also, create a function `sum_of_primes(primes)` to calculate the sum of all prime numbers in the generated sequence. The input range will be provided by the user, and it should be validated to ensure that `start` is smaller than `end`. The functions should be designed to handle large input ranges efficiently and minimize time and space complexity.
"""

def sieve_of_eratosthenes(start, end):
    primes = []
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    for i in range(start, end + 1):
        if is_prime[i]:
            primes.append(i)

    return primes