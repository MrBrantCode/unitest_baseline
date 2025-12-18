"""
QUESTION:
Write a function `is_armstrong_prime_palindrome(num)` that takes an integer as input and returns a boolean value indicating whether the number is an Armstrong number, a prime number, a palindrome, and a perfect square, and has exactly three unique digits. The input number should be a positive integer with three or fewer digits.
"""

def is_armstrong_prime_palindrome(num):
    # Check if the input is a positive integer
    if not isinstance(num, int) or num <= 0:
        return False

    # Check if the input has more than three digits
    if num > 999:
        return False

    # Check if the input is a prime number
    if not is_prime(num):
        return False

    # Check if the input has exactly three unique digits
    digits = set(str(num))
    if len(digits) != 3:
        return False

    # Check if the input is an Armstrong number
    num_str = str(num)
    power = len(num_str)
    digit_sum = sum(int(digit) ** power for digit in num_str)
    if digit_sum != num:
        return False

    # Check if the input is a palindrome
    if num_str != num_str[::-1]:
        return False

    # Check if the input is a perfect square
    if int(num ** 0.5) ** 2 != num:
        return False

    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True