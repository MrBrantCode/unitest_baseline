"""
QUESTION:
Write a function `identify_primes(array)` that takes a list of integers as input, identifies the prime numbers, and returns them as a list. The input list may contain any non-negative integers, and the function should handle numbers that are not prime. Note that the function does not need to be optimized for very large numbers, but it should work correctly for the given input range.
"""

def identify_primes(array):
    primes = []
    for num in array:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes