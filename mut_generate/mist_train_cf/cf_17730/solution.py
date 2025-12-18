"""
QUESTION:
Write a function `sum_of_primes_in_reverse` that takes an array of integers as input and returns the sum of all prime numbers in the array. The function should iterate through the array in reverse order, only considering prime numbers in the calculation. Assume the input array is not empty and contains at least one integer.
"""

def sum_of_primes_in_reverse(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in reversed(arr) if is_prime(num))