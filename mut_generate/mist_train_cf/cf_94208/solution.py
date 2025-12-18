"""
QUESTION:
Write a function `fibonacci_sum(n)` that calculates the sum of the Fibonacci sequence up to the nth term, excluding any term that is divisible by 5. The Fibonacci sequence starts with 0 and 1.
"""

def fibonacci_sum(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    
    fib_n_minus_1 = 0 
    fib_n_minus_2 = 1 
    fib_sum = 0
    
    # Generate Fibonacci sequence up to the nth term
    for _ in range(2, n+1):
        current_fib = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_1 = fib_n_minus_2
        fib_n_minus_2 = current_fib
        
        # Exclude terms divisible by 5
        if current_fib % 5 != 0:
            fib_sum += current_fib

    return fib_sum + 1