"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using a for loop. The function should take an integer `n` as input, where `n` is a non-negative integer. The function should return the nth Fibonacci number if `n` is non-negative, and handle the case when `n` is negative.
"""

def fibonacci(n):
    if n < 0:
        print("Invalid Input")
        return
    
    num1, num2 = 0, 1

    if n == 0:
        return num1
    elif n == 1:
        return num2
    else:
        for i in range(2, n+1):
            next_num = num1 + num2
            num1, num2 = num2, next_num
        return num2