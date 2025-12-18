"""
QUESTION:
Create a function named `generate_fibonacci` that generates a Fibonacci sequence up to the nth number. The function should take an integer `n` as input, return a list of integers representing the Fibonacci sequence, and have a time complexity of O(n) and a space complexity of O(1). If `n` is not a positive integer, the function should return an error message.
"""

def generate_fibonacci(n):
    # Handle invalid inputs
    if not isinstance(n, int) or n < 1:
        return "Invalid input. Please enter a positive integer."
    
    # Base cases
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence