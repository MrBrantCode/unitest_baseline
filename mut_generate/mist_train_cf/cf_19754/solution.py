"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and prints all numbers in the Fibonacci series up to `n` that are both prime numbers and perfect squares.
"""

def fibonacci(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_perfect_square(num):
        root = int(num**0.5)
        return root**2 == num

    fib_series = [0, 1]
    while fib_series[-1] < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    for num in fib_series:
        if is_prime(num) and is_perfect_square(num):
            print(num)