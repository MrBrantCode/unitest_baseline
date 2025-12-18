"""
QUESTION:
Write a function named 'fibonacci' that generates the Fibonacci sequence up to the nth term without using recursion or any additional data structures, with a time complexity of O(n). The function should take an integer 'n' as input and return a list of Fibonacci numbers. The function should handle invalid inputs where 'n' is less than or equal to 0.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence