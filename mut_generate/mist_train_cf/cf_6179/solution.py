"""
QUESTION:
Write a function `sum_unique_primes` that takes a list of integers as input and returns the sum of all unique prime numbers in the list. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the number of unique prime numbers in the input list, without using any built-in functions or libraries for prime number calculation.
"""

def sum_unique_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = set()
    total_sum = 0
    for num in lst:
        if is_prime(num) and num not in primes:
            primes.add(num)
            total_sum += num
    return total_sum