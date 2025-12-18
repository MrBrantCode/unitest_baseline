"""
QUESTION:
Implement a function called `print_primes` that takes two parameters: `start` and `end`, representing the range of numbers to check for prime numbers. The function should print all prime numbers within that range. A prime number is a number greater than 1 that is divisible only by 1 and itself. The solution should have a time complexity of O(n * sqrt(m)), where n is the number of elements in the range and m is the largest number in the range. Do not use external libraries or built-in functions that directly give prime numbers.
"""

import math

def print_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(start, end + 1):
        if is_prime(num):
            print(f"{num} is prime")