"""
QUESTION:
Define a function `multiply_primes_even(num1, num2)` that takes two numbers as arguments and returns their product if both numbers are prime and even. Otherwise, it should return a message indicating that both numbers must be prime and even. Assume a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(number):
    """
    Helper function to check if a number is prime.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def multiply_primes_even(num1, num2):
    """
    Function to multiply two numbers, but only works if both numbers are prime and even.
    """
    if is_prime(num1) and is_prime(num2) and num1 % 2 == 0 and num2 % 2 == 0:
        return num1 * num2
    else:
        return "Both numbers must be prime and even."