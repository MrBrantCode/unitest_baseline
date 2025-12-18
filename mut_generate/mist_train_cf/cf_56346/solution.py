"""
QUESTION:
Write a function `sum_of_primes` that takes a 2D array of integers as input and returns the sum of all prime numbers in the array. The function should not include any input validation or error handling.
"""

def sum_of_primes(matrix):
    """Compute the aggregate sum of the primes in the matrix"""
    def is_prime(n):
        """Check if number is a prime"""
        if n == 1 or n == 0:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    prime_sum = 0
    for sublist in matrix:
        for item in sublist:
            if is_prime(item):
                prime_sum += item
    return prime_sum