"""
QUESTION:
Create a function named `FibonacciSum` that takes an integer `n` as input and returns the sum of the Fibonacci sequence up to the nth number. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. If `n` is less than 0, the function should return an error message.
"""

def FibonacciSum(n): 
    fib1 = 0
    fib2 = 1
    if n < 0: 
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1: 
        return 0
    else: 
        sum = 0
        for i in range(2,n+1): 
            fib_n = fib1 + fib2
            fib1 = fib2
            fib2 = fib_n
            sum = sum + fib_n
        return sum + fib2