"""
QUESTION:
Design a function named `prime_cubed_positions` that takes two integers `start` and `end` as input and returns two lists. The first list should contain the cubes of integers within the range `[start, end]`. The second list should contain the positions (0-indexed) of prime numbers in the list of cubes. The function should return empty lists if `end` is less than `start`.
"""

def prime_cubed_positions(start, end):
    """Return the cubes of integers within a range [start, end] and 
    the positions of cubed primes in the list.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if end < start:
        return [], []

    cubes = [i ** 3 for i in range(start, end+1)]
    prime_positions = [i for i, n in enumerate(cubes) if is_prime(n)]
    return cubes, prime_positions