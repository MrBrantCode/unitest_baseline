"""
QUESTION:
Write a function `factorial_if_divisible` that takes an integer `number` as input. If the number is divisible by both 3 and 5, calculate and print the factorial of the number.
"""

def factorial_if_divisible(number):
    if (number % 3 == 0) and (number % 5 == 0):
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial