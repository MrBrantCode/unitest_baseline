"""
QUESTION:
Write a function named `is_prime_and_fibonacci` that takes no arguments, and prints prime numbers between 20 and 50 (inclusive) along with a message indicating whether each prime number is also a Fibonacci number. 

The function should use helper functions `is_prime(n)` to check if a number `n` is prime, and `is_fibonacci(n)` to check if a number `n` is a Fibonacci number. The `is_fibonacci(n)` function should utilize an `is_square(n)` helper function to check if a number `n` is a perfect square.
"""

import math

# Function to check perfect square
def is_square(n):
    x = int(math.sqrt(n))
    return n == x * x

# Function to check fibonacci number
def is_fibonacci(n):
    x = 5 * n**2
    return is_square(x + 4) or is_square(x - 4)

# Function to check prime number
def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# Function to print prime numbers and check if fibonacci
def is_prime_and_fibonacci():
    for i in range(20, 51):
        if is_prime(i):
            print(i, 'is a prime number')
            if is_fibonacci(i):
                print(i, 'is also a fibonacci number')
            else:
                print(i, 'is not a fibonacci number')