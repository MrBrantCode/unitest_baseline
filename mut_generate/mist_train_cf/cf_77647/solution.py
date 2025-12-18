"""
QUESTION:
Write a function named `primes_in_lst` that takes an integer array as input and returns an array of boolean values of the same length. The boolean value at each index in the output array should indicate whether the corresponding integer in the input array is a prime number (True) or not (False). The function should be optimized for performance efficiency when handling large numbers.
"""

def primes_in_lst(lst):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    return [is_prime(x) for x in lst]