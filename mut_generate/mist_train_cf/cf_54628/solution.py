"""
QUESTION:
Create a function named `find_primes` that takes three parameters: an integer `start`, an integer `end`, and an integer `num`. This function should return a list of all prime numbers within the range from `start` to `end` (inclusive) that evenly divide `num`. The range is 1-indexed and `start` is less than or equal to `end`.
"""

def find_primes(start, end, num):
    """
    Returns a list of prime numbers within the range from start to end (inclusive) that evenly divide num.

    Args:
        start (int): The start of the range (1-indexed).
        end (int): The end of the range.
        num (int): The number that the primes should divide evenly.

    Returns:
        list: A list of prime numbers in the range that divide num evenly.
    """
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True

    prime_nums = [i for i in range(start, end + 1) if is_prime(i) and num % i == 0]
    return prime_nums