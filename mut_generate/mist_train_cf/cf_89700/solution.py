"""
QUESTION:
Implement a function called `get_primes` that takes in an integer `n` and returns a tuple containing a list of all prime numbers up to `n` and the total count of prime numbers found. The function should use the Sieve of Eratosthenes algorithm with a time complexity of O(n log(log n)), and it should handle very large numbers efficiently without causing memory overflow or taking excessive time to execute. If `n` is less than 2, return an empty list and 0. The function should have type hints for the parameter and return value. The return type should be a tuple of a list of integers and an integer.
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