"""
QUESTION:
Write a function named `prime_factorial` that calculates the factorial of all prime numbers within a specified range `r` (inclusive) and returns or prints the results. The function should be able to handle any positive integer range.
"""

def prime_factorial(r):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                return True
        return False

    for i in range(r+1):  # loop through the range inclusively
        if is_prime(i):
            print(f'Factorial of {i} is {factorial(i)}')