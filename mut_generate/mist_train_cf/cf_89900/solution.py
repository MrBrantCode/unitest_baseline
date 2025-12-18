"""
QUESTION:
Write a function called `sum_odd_digits` that calculates the sum of the products of the odd digits of a given number with its reverse, excluding any odd digits that are prime numbers. The function should return -1 if there are no odd digits in the number or if all the odd digits are prime numbers. The input number is guaranteed to be between 10^2 and 10^9 (inclusive) and will have at least 3 digits.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_number(num):
    return int(str(num)[::-1])

def sum_odd_digits(num):
    result = 0
    reversed_num = reverse_number(num)
    for i, digit in enumerate(str(num)):
        digit = int(digit)
        if digit % 2 == 0 or is_prime(digit):
            continue
        result += digit * int(str(reversed_num)[i])
    if result == 0:
        return -1
    return result