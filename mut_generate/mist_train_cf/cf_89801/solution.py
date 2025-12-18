"""
QUESTION:
Write a function named `prime_sum` that takes a list of integers as input and returns the sum of all prime numbers in the list that are greater than 100 and less than 1000. The output should be a single integer representing the sum of the prime numbers. The function should not return the individual prime numbers, only their sum.
"""

def prime_sum(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in lst if 100 < num < 1000 and is_prime(num)]
    return sum(primes)