"""
QUESTION:
Write a function named `print_primes` that takes an integer `n` as input and prints out all the prime numbers up to and including `n`. The function should handle invalid inputs (non-integer values or numbers less than 1) by printing "Invalid input" and returning early. The time complexity of the solution should be O(n * sqrt(m)), where n is the input number and m is the largest prime number up to n, and the space complexity should be O(1).
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