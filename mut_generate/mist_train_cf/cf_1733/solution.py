"""
QUESTION:
Write a Python function named `is_prime` to check if a number is prime and a main program to take two inputs, `number1` and `number2`, between 1 and 1000 (inclusive). The program should print their multiplication, check if the numbers are prime, check if their multiplication is divisible by 5, and calculate the sum of all prime numbers between `number1` and `number2`.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True