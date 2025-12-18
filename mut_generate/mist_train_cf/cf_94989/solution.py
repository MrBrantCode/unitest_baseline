"""
QUESTION:
Implement a function called `print_primes` that takes in two parameters: `start` and `end`, representing the range of numbers to check. The function should print out all the prime numbers within that range. A prime number is a number greater than 1 that is divisible only by 1 and itself. The solution should have a time complexity of O(n * sqrt(m)), where n is the number of elements in the range (end - start + 1) and m is the largest number in the range.
"""

import math

def print_primes(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    for num in range(start, end + 1):
        if is_prime(num):
            print(f"{num} is prime")