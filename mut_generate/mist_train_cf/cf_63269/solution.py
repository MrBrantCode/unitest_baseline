"""
QUESTION:
Write a function called `factorize` that takes an integer `n` where 2 ≤ n ≤ 10^6, performs prime factorization on it, and returns a tuple containing a list of prime factors in the order of their appearance, a dictionary displaying the frequency of each factor, and a dictionary with the primality test result for each factor. The list of prime factors should be able to be multiplied together to get the original number `n`.
"""

from typing import List, Tuple, Dict
import math

def factorize(n: int) -> Tuple[List[int], Dict[int, int], Dict[int, bool]]:
    """
    Returns a prime factor list and a dictionary displaying the frequency of each factor in the decomposition process,
    Perform primality testing on each factor.

    Factors should be listed according to their frequency of appearance in the decomposition process.
    The entered number (2 ≤ n ≤ 10^6) should be the product of all factors.
    """
    
    factors = []
    freq = {}
    primes = {}

    # Prime factorization
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(int(i))
            n = n / i
    if n > 2:
        factors.append(int(n))

    # count the frequency of each factor
    for factor in factors:
        if factor not in freq:
            freq[factor] = 1
        else:
            freq[factor] += 1

    # perform primality check on each factor
    def is_prime(n: int) -> bool:
        """Check if n is a prime number"""
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(math.sqrt(n)+1)):
                if n % i == 0:
                    return False
            return True

    for factor in freq.keys():
        primes[factor] = is_prime(factor)

    return [factors, freq, primes]