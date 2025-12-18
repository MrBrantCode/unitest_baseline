"""
QUESTION:
Create a function called `print_primes(n)` that prints all prime numbers up to and including the provided integer `n`. The function must handle invalid inputs and check for primality with a time complexity of O(n * sqrt(m)), where n is the input number and m is the largest prime number up to n. The space complexity should be O(1).
"""

import math

def print_primes(n):
    if not isinstance(n, int) or n < 1:
        print("Invalid input")
        return
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
            print(i, end=" ")
    print()