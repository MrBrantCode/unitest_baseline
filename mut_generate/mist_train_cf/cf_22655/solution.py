"""
QUESTION:
Create a function `remove_duplicates_and_primes` that takes a list of integers as input. The function should return a new list containing only the unique prime elements from the input list. The function should exclude non-prime numbers and duplicates.
"""

def remove_duplicates_and_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return list(set([num for num in lst if is_prime(num)]))