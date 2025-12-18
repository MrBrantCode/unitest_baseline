"""
QUESTION:
Write a function `solution` that takes an integer `n` as input and returns a string stating whether the factorial of `n` is a prime number or not. The function should use a recursive function to calculate the factorial of `n` and another function to check if a number is prime. The factorial of `n` (n!) is a product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n-1)

def is_prime(n):
    if n == 1 or n == 0: 
        return False
    else:
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return False
        return True

def solution(n):
    fact = factorial(n)
    if is_prime(fact):
        return "The factorial of " + str(n) + " is " + str(fact) + " and it is a prime number."
    else:
        return "The factorial of " + str(n) + " is " + str(fact) + " and it is not a prime number."