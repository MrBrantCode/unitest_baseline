"""
QUESTION:
Write a function `is_prime(number)` that takes an integer `number` as input and returns a boolean value indicating whether the number is prime or not. The function should use an if-else statement in its implementation. Assume that the input number is a non-negative integer. The function should optimize the calculation by checking for factors up to the square root of the number.
"""

def is_prime(number):
    # Prime numbers are greater than 1
    if number > 1:
        # Check for factors from 2 to the square root of the number
        for i in range(2, int(number**0.5) + 1):
            # If the number is divisible by any other number, it's not prime
            if number % i == 0:
                return False
        # If no factors are found, the number is prime
        return True
    # Numbers less than or equal to 1 are not prime
    else:
        return False