"""
QUESTION:
Write a function `check_number` that checks if an integer is a palindrome, a prime number, and divisible by a specific integer in a given base. The function should be able to handle integers with up to 1000 digits and be optimized for time complexity. It should return a tuple containing the original number, its base, whether it is a palindrome, whether it is a prime number, and whether it is divisible by the specific divisor.

Implement the function in Python and include helper functions `is_palindrome`, `is_prime`, and `is_divisible`. The `is_palindrome` function should take an integer and its base as input, the `is_prime` function should take an integer as input, and the `is_divisible` function should take an integer and a divisor as input.

Additionally, write a function `print_table` that prints a LaTeX table of the results for a list of numbers in a given base and with a specific divisor.
"""

def check_number(number, base=10, divisor=None):
    def is_palindrome(number, base=10):
        if base == 10:
            number_str = str(number)
        else:
            number_str = hex(number)[2:] if base == 16 else bin(number)[2:]
        return number_str == number_str[::-1]

    def is_prime(number):
        import math
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def is_divisible(number, divisor):
        return number % divisor == 0

    palindrome = is_palindrome(number, base)
    prime = is_prime(number)
    divisible = is_divisible(number, divisor) if divisor else None
    return (number, base, palindrome, prime, divisible)