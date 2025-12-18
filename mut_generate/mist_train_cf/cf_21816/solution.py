"""
QUESTION:
Write a function named `is_prime()` that checks whether a given number is prime or not and returns a boolean value. Implement another function to prompt the user for a range of numbers, validate the input, and print out all prime numbers within that range. The program should also display the total number of prime numbers found. The input validation should ensure that the starting number is smaller than the ending number and both numbers are positive integers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True