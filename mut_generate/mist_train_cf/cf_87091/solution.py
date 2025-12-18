"""
QUESTION:
Create a function `sum_even_fibonacci(limit)` that calculates the sum of all even Fibonacci numbers less than the given limit without using any additional data structures to store the Fibonacci sequence. The function should return the sum of these even Fibonacci numbers.
"""

def sum_even_fibonacci(limit):
    # Initialize variables
    sum = 0
    current_fib = 2
    previous_fib = 1

    # Iterate through the Fibonacci sequence
    while current_fib < limit:
        # Check if current Fibonacci number is even
        if current_fib % 2 == 0:
            sum += current_fib
        
        # Calculate the next Fibonacci number
        next_fib = current_fib + previous_fib
        
        # Update previous and current Fibonacci numbers
        previous_fib = current_fib
        current_fib = next_fib
    
    return sum