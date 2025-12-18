"""
QUESTION:
Create a function `fib_primes(n)` to generate a Fibonacci sequence up to the n-th number and return a list of prime numbers found in that sequence. The function should handle edge cases such as 0 and 1, and print the number of prime numbers found in the sequence. The time complexity of the solution should not exceed O(n log(n)).
"""

import math

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fib_primes(n):
    if n < 2:
        return []
    fib_sequence = [0, 1]
    while len(fib_sequence) < n+1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_prime = [num for num in fib_sequence if is_prime(num)]
    print("Number of prime numbers in Fibonacci sequence up to n is: ", len(fib_prime))
    return fib_prime