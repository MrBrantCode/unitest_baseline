"""
QUESTION:
Write a function `fibonacci_sum` that calculates the sum of the first n Fibonacci numbers. The function should take a positive integer n as input and return the sum as output. The time complexity of the function should be O(n) and it should not use any built-in functions or libraries to calculate the Fibonacci sequence.
"""

def fibonacci_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_sequence = [0, 1]
    fib_sum = 1

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        fib_sum += fib_sequence[i]
    
    return fib_sum