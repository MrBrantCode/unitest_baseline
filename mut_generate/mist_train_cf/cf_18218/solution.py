"""
QUESTION:
Write a function `fibonacci(n)` that generates the nth Fibonacci number using a loop and returns -1 for invalid inputs (n < 0). The function should have a time complexity of O(n).
"""

def fibonacci(n):
    if n < 0:
        return -1  # Return -1 for invalid inputs
    
    if n <= 1:
        return n  # Return n for n = 0 or n = 1
    
    # Initialize variables to store the two previous Fibonacci numbers
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    
    # Calculate the nth Fibonacci number iteratively
    for _ in range(2, n+1):
        fib_n = fib_n_minus_2 + fib_n_minus_1
        
        # Update the two previous Fibonacci numbers
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    
    return fib_n