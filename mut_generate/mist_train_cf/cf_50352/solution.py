"""
QUESTION:
Write a function named `sum_primes_at_multiple_of_four` that calculates the sum of prime numbers at indices that are multiples of 4 in a given array of integers. The function should return the sum of these prime numbers.
"""

def sum_primes_at_multiple_of_four(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    return sum(num for index, num in enumerate(arr) if index % 4 == 0 and is_prime(num))