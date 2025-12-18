"""
QUESTION:
Write a function `fibonacciSum` that takes an integer `n` as input. The function should calculate the sum of Fibonacci numbers less than `n` that are divisible by 3 or 5 and end in 3 or 7. The function should return the sum of these Fibonacci numbers.
"""

def fibonacciSum(n):
    a = 0
    b = 1
    sum = 0
    while a < n:
        if (a % 3 == 0 or a % 5 == 0) and (a % 10 == 3 or a % 10 == 7):
            sum += a
        temp = a
        a = b
        b = temp + b
    return sum