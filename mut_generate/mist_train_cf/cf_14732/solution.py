"""
QUESTION:
Write a function named `check_prime` that takes an integer `number` as input and determines whether it is a prime number. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The function should return "Number is a prime number" if the input is prime and "Number is not a prime number" otherwise. The function should use a loop and a conditional statement to check for primality, and it should only iterate up to the square root of the input number.
"""

def check_prime(number):
    """
    This function checks if a given number is prime or not.

    Args:
        number (int): The number to be checked.

    Returns:
        str: "Number is a prime number" if the number is prime, "Number is not a prime number" otherwise.
    """

    if number <= 1:
        return "Number is not a prime number"
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return "Number is not a prime number"
        return "Number is a prime number"