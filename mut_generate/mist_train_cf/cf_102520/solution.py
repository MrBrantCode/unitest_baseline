"""
QUESTION:
Write a function named `is_prime` to determine whether a number is prime, and use it to print out all prime numbers between 1 and 100 in ascending order. The `is_prime` function should take an integer `n` as input and return a boolean indicating whether `n` is prime. It should be efficient and able to handle large numbers. The main part of the program should iterate over numbers from 1 to 100, check if each number is prime using the `is_prime` function, and print the prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True