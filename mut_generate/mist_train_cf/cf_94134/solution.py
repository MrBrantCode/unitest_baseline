"""
QUESTION:
Write a function `print_numbers()` that prints all numbers from 1 to 100 that are divisible by either 7 or 9, but not both. The function should ensure that each number is only checked once for divisibility and should not use the modulo operator (%).
"""

def is_divisible(number, divisor):
    return number // divisor * divisor == number

def print_numbers():
    for number in range(1, 101):
        if (is_divisible(number, 7) or is_divisible(number, 9)) and not (is_divisible(number, 7) and is_divisible(number, 9)):
            print(number)