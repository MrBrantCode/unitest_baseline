"""
QUESTION:
Write a function named `fibonacci_recursive` that calculates the nth Fibonacci number using memoization to optimize efficiency. The function should take an integer `n` as input and return the corresponding Fibonacci number. It should handle cases where `n` is less than or equal to 0, and it should store previously calculated Fibonacci numbers to avoid redundant calculations.
"""

# Dictionary to store the already calculated Fibonacci numbers
fib_dict = {}

def fibonacci_recursive(n):
    # Base cases
    if n <= 0:
        return "Input should be a positive integer"
    elif n <= 2:
        return 1
    
    # Check if the Fibonacci number is already calculated
    if n in fib_dict:
        return fib_dict[n]
    
    # Calculate the Fibonacci number recursively
    fib_number = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
    # Store the calculated Fibonacci number in the dictionary
    fib_dict[n] = fib_number
    
    return fib_number