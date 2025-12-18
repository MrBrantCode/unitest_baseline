"""
QUESTION:
Create a function `fibonacci_numbers_divisible_by_three` that generates the first n Fibonacci numbers that are divisible by 3. The function should take one argument, n, representing the number of Fibonacci numbers to generate.
"""

def fibonacci_numbers_divisible_by_three(n):
    fib_numbers = []
    a, b = 0, 1
    count = 0
    while count < n:
        if a % 3 == 0:
            fib_numbers.append(a)
            count += 1
        a, b = b, a + b
    return fib_numbers