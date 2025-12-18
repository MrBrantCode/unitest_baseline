"""
QUESTION:
Define a function named `multiply_primes_even` that takes two integers as arguments and returns their product if both numbers are prime and even. If the numbers do not meet these conditions, the function should return an error message. The function should assume that prime numbers are greater than 1 and can be even (i.e., the number 2 is considered a prime number).
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def multiply_primes_even(num1, num2):
    if is_prime(num1) and is_prime(num2) and num1 % 2 == 0 and num2 % 2 == 0:
        return num1 * num2
    else:
        return "Both numbers must be prime and even."