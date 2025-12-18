"""
QUESTION:
Implement a function `is_divisible(num, divisor)` that checks if a number `num` is divisible by another number `divisor` without using any mathematical operators or built-in functions for division or multiplication. Use this function to create a FizzBuzz game that prints the numbers from 1 to 100, replacing numbers divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz", and numbers divisible by both 3 and 5 with "FizzBuzz".
"""

def is_divisible(num, divisor):
    while num >= divisor:
        num -= divisor
    return num == 0