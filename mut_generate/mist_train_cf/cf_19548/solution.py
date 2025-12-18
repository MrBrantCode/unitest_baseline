"""
QUESTION:
Write a function `print_primes(n)` that prints all prime numbers up to and including the provided integer `n`. The function should handle invalid inputs such as non-integer values or negative numbers by printing "Invalid input" and returning early. The function should optimize its primality check to have a time complexity of O(sqrt(n)).
"""

import math

def print_primes(n):
    if type(n) != int or n < 1:
        print("Invalid input")
        return
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
            print(i, end=" ")
    print()