"""
QUESTION:
Write a function named `function` that takes a positive integer `n` as input and returns the sum of the first `n` Fibonacci numbers. The function should not accept non-integer or non-positive inputs, and should return an error message in such cases.
"""

def function(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input. Please enter a positive integer."
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return sum(fib_list[:n])