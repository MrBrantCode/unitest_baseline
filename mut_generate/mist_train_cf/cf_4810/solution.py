"""
QUESTION:
Write a program with a function `find_next_primes(num, count)` that takes two parameters: a positive integer `num` and an integer `count`. The function should return the first `count` prime numbers after `num`. The program should handle cases where `num` is negative or zero, returning an error message. The prime number checking algorithm should have a time complexity of O(√m) for checking if a number `m` is prime, where the time complexity is calculated based on the number being checked for primality.
"""

import math

def find_next_primes(num, count):
    if num <= 0:
        return "Input number must be a positive integer."
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    next_num = num + 1
    while len(primes) < count:
        if is_prime(next_num):
            primes.append(next_num)
        next_num += 1
    return primes