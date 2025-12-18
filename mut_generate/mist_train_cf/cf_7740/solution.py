"""
QUESTION:
Create a function `is_divisible(numerator, divisor)` that checks if `numerator` is divisible by `divisor` using only bitwise operators and no mathematical operators or built-in functions like division or multiplication. Implement this function in a FizzBuzz game that prints the numbers from 1 to 100, replacing all the numbers divisible by 3 with the word "Fizz", the numbers divisible by 5 with the word "Buzz", and the numbers divisible by both 3 and 5 with the word "FizzBuzz".
"""

def is_divisible(numerator, divisor):
    while numerator >= divisor:
        numerator -= divisor
    return numerator == 0