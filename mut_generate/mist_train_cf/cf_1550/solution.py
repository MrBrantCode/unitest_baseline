"""
QUESTION:
Write a function named `is_prime(number)` that takes an integer `number` as input and returns `True` if the number is prime, and `False` otherwise. A prime number is greater than 1 and has no divisors other than 1 and itself. Implement a loop with an early exit condition to improve efficiency. Use this function to calculate the average of prime numbers in a given list, excluding non-prime numbers from the calculation. The input list may contain integers greater than 1.
"""

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True