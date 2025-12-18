"""
QUESTION:
Generate a function named `generate_primes(n)` that returns a list of prime numbers from 1 to n, excluding multiples of 3, with a time complexity of O(n) and a space complexity of O(n).
"""

def generate_primes(n):
    """
    Generate a list of prime numbers from 1 to n, excluding multiples of 3.

    Args:
        n (int): The upper limit of the range.

    Returns:
        list: A list of prime numbers from 1 to n, excluding multiples of 3.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            if i % 3 != 0:  # Exclude multiples of 3
                for j in range(i*i, n+1, i):
                    primes[j] = False

    prime_list = []
    for i in range(2, n+1):
        if primes[i] and i % 3 != 0:  # Exclude multiples of 3
            prime_list.append(i)

    return prime_list