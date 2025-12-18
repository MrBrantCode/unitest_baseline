"""
QUESTION:
Develop a function named `largest_missing_prime` that takes a sorted list of prime numbers as input and returns the largest prime number that is missing from the list. The function should iterate through the list and identify gaps between consecutive prime numbers. It should then check which of the numbers in these gaps are prime and return the largest one. If no missing prime numbers are found, the function should return -1.
"""

def largest_missing_prime(primes):
    def is_prime(n):
        if n < 2:
            return False
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                return False
        return True

    largest_missing = -1
    for i in range(1, len(primes)):
        for j in range(primes[i-1] + 2, primes[i], 2):
            if is_prime(j):
                largest_missing = max(largest_missing, j)
    return largest_missing