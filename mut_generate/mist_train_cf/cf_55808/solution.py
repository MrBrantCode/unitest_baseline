"""
QUESTION:
Construct a function `fibonacci(n)` that generates an array of the first n figures in the Fibonacci sequence. The function should handle exceptional cases where n is outside the valid range. The input n is restricted to a non-negative integer not exceeding 100.
"""

def fibonacci(n):
    # Check for invalid values
    if n < 0 or n > 100:
        return "Input must be between 0 and 100."

    # declare a list and populate the initial positions
    fib_list = [0, 1] + [0]*(n-2)
    
    # populate the list from third position to nth position
    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]  

    return fib_list[:n]