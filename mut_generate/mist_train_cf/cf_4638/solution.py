"""
QUESTION:
Write a function `is_narcissistic_number` that takes an integer as input and returns True if it is a Narcissistic number, and False otherwise. A Narcissistic number is a number that is equal to the sum of its own digits raised to the power of the number of digits, where the power is a prime number.
"""

def is_narcissistic_number(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    is_prime = True
    for i in range(2, int(num_digits ** 0.5) + 1):
        if num_digits % i == 0:
            is_prime = False
            break
    if not is_prime or num_digits < 2:
        return False
    narcissistic_sum = sum([digit ** num_digits for digit in digits])
    return narcissistic_sum == number