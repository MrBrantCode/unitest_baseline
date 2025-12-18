"""
QUESTION:
Write a function `sum_primes` that takes a list of integers as input, sorts the list in ascending order, and returns the sum of all prime numbers greater than 10 that are not divisible by any number in the list that comes before it. The function should use a recursive approach to determine whether a given number is prime or not.
"""

def sum_primes(lst):
    def is_prime(n, primes):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        for j in primes:
            if j < n and n % j == 0:
                return False
        return True

    lst.sort()
    primes = []
    for i in lst:
        if i > 10 and is_prime(i, primes):
            primes.append(i)
    return sum(primes)