"""
QUESTION:
Create a function called `fibonacci(n)` that generates the n-th Fibonacci number using recursion and memoization. The function should be able to handle large values of n (n > 10^6) without causing a stack overflow. The function should optimize recursive calls by storing and reusing previously calculated Fibonacci numbers.
"""

# Memoization dictionary to store already calculated Fibonacci numbers
fib_dict = {}

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Check if Fibonacci number already calculated and stored in the dictionary
    if n in fib_dict:
        return fib_dict[n]
    
    # Calculate the Fibonacci number using recursion and memoization
    fib_number = fibonacci(n-1) + fibonacci(n-2)
    
    # Store the calculated Fibonacci number in the dictionary
    fib_dict[n] = fib_number
    
    return fib_number