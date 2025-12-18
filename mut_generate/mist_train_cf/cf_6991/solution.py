"""
QUESTION:
Implement a class with a method called `get_primes` that takes an integer `n` as input and returns a tuple containing a list of all prime numbers up to `n` and the total count of prime numbers found. The method should use the Sieve of Eratosthenes algorithm with a time complexity of O(n log(log n)), handle very large numbers efficiently, and include type hints for the parameter and return value. If `n` is less than 2, return an empty list and 0.
"""

def get_primes(n: int) -> tuple[list[int], int]:
    if n < 2:
        return [], 0

    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = False

    for num in range(int(n ** 0.5) + 1, n + 1):
        if is_prime[num]:
            primes.append(num)

    return primes, len(primes)