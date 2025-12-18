"""
QUESTION:
Create a function `sum_of_cubes(n)` that calculates the sum of the cubes of the first `n` prime numbers, excluding 2 and 3. The prime numbers must be generated using the Sieve of Eratosthenes algorithm. The function should take a positive integer `n` as input and return the sum of the cubes of the first `n` prime numbers, excluding 2 and 3.
"""

def sum_of_cubes(n):
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, n + 1) if is_prime[i]]

    primes = sieve_of_eratosthenes(n * 10 + 3)  # Generating prime numbers up to n*10+3 to exclude 2 and 3
    prime_cubes = [prime ** 3 for prime in primes[2:]]

    return sum(prime_cubes[:n])