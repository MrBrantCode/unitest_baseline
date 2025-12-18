"""
QUESTION:
Write a function named `sum_even_fibonacci` that takes an integer `limit` as input and returns the sum of all even Fibonacci numbers less than the given limit, using an iterative approach and without using any additional data structures to store the Fibonacci sequence.
"""

def sum_even_fibonacci(limit):
    sum = 0
    current_fib = 2
    previous_fib = 1

    while current_fib < limit:
        if current_fib % 2 == 0:
            sum += current_fib
        
        next_fib = current_fib + previous_fib
        
        previous_fib = current_fib
        current_fib = next_fib
    
    return sum