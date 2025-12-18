"""
QUESTION:
Create a function `sum_of_distinct_primes` that takes a list of integers as input and returns the sum of the distinct prime numbers present in the list. The function should not include non-prime numbers or duplicate prime numbers in the sum.
"""

def sum_of_distinct_primes(lst):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    distinct_primes = set()
    for i in lst:
        if i > 1 and is_prime(i):
            distinct_primes.add(i)

    return sum(distinct_primes)