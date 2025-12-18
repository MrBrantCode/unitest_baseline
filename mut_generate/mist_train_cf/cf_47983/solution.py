"""
QUESTION:
Write a function to count the number of prime numbers in a given list of integers. The function should take a list as input and return the count of prime numbers. The list can contain duplicate values and can be of any length. The function should be able to handle large numbers efficiently.
"""

def count_primes_in_list(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(is_prime(i) for i in lst)