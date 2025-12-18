"""
QUESTION:
Write a function `analyze_sum(num1, num2)` that takes two numbers as input and performs the following operations based on their sum:
- Print whether the sum is even or odd.
- Print whether the sum is a prime number.
- Print whether the sum is a perfect square.
- Print whether the sum is a Fibonacci number.
- Print whether the sum is divisible by both numbers, only one of them, or neither.
"""

import math

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect_square(number):
    sqrt = math.sqrt(number)
    return sqrt == int(sqrt)

def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number

def is_divisible_by(number, divisor):
    return number % divisor == 0

def analyze_sum(num1, num2):
    sum = num1 + num2
    
    if is_even(sum):
        print("The sum is even")
    else:
        print("The sum is odd")
        
    if is_prime(sum):
        print("The sum is a prime number")
        
    if is_perfect_square(sum):
        print("The sum is a perfect square")
        
    if is_fibonacci(sum):
        print("The sum is a Fibonacci number")
        
    if is_divisible_by(sum, num1) and is_divisible_by(sum, num2):
        print("The sum is divisible by both numbers")
    elif is_divisible_by(sum, num1) or is_divisible_by(sum, num2):
        print("The sum is divisible by one of the numbers")
    else:
        print("The sum is not divisible by either of the numbers")