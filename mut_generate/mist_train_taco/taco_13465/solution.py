"""
QUESTION:
It is known that even numbers greater than or equal to 4 can be represented by the sum of two prime numbers. This is called the Goldbach's conjecture, and computer calculations have confirmed that it is correct up to a fairly large number. For example, 10 can be represented by the sum of two prime numbers, 7 + 3 and 5 + 5.

Write a program that inputs the integer n and outputs how many combinations of n are the sum of two prime numbers. However, n must be 4 or more and 50,000 or less. Also, the n entered is not always even.



Input

Given multiple datasets. Each dataset is given n on one row. When n is 0, it is the last input. The number of datasets does not exceed 10,000.

Output

For each dataset, output the number of combinations in which n is the sum of two prime numbers on one line.

Example

Input

10
11
0


Output

2
0
"""

import bisect
from itertools import compress

def sieve_of_eratosthenes(limit):
    """Generate a list of primes up to the given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def count_goldbach_combinations(n):
    """
    Count the number of combinations of two prime numbers that sum up to the given integer n.
    
    Parameters:
    n (int): The integer for which to count the combinations.
    
    Returns:
    int: The number of combinations of two prime numbers that sum up to n.
    """
    if n < 4 or n > 50000:
        raise ValueError("n must be between 4 and 50000 inclusive.")
    
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    count = 0
    
    for prime in primes:
        if prime > n // 2:
            break
        if (n - prime) in prime_set:
            count += 1
    
    return count