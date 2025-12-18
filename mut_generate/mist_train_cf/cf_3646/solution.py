"""
QUESTION:
Create a function called `is_armstrong_prime_palindrome` that takes a single integer argument. The function should return `True` if the number is a positive integer with exactly three digits, is prime, has exactly three unique digits, is an Armstrong number (sum of its digits raised to the power of the number of digits is equal to the original number), is a palindrome (reads the same backwards as forwards), and is a perfect square. Otherwise, return `False`.
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