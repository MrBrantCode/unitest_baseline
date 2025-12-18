"""
QUESTION:
Implement the `sieve_of_eratosthenes` function to find all prime numbers up to a given limit.

The function takes an integer `limit` as input and returns a list of all prime numbers up to the given `limit`. The input limit will be in the range of `2` to `10^5`. The solution should have a time complexity of O(n*log(log(n))), where n is the input limit.
"""

from typing import List

def sieve_of_eratosthenes(limit: int) -> List[int]:
    # Create a boolean array to keep track of whether each number is prime or not
    is_prime = [True] * (limit + 1)

    # Set the first two numbers (0 and 1) as not prime
    is_prime[0] = is_prime[1] = False

    # Iterate from 2 to the square root of the limit
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i greater than or equal to i*i as not prime
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    # Iterate through the boolean array and append all the indices with True values to the result list
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes