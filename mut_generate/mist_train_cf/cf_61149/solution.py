"""
QUESTION:
Create a function called `fibonacci_product` that takes two parameters `start` and `end` representing an inclusive interval. The function should return the product of all Fibonacci numbers within the given interval, where the Fibonacci sequence starts from 0 and 1. The interval is 0-indexed, meaning it starts from 0 as the first Fibonacci number.
"""

def fibonacci_product(start, end):
    fib_numbers = [0, 1]
    for i in range(2, end+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    product = 1
    for i in range(start, end+1):
        product *= fib_numbers[i]
    return product