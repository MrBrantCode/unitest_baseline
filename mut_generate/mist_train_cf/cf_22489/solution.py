"""
QUESTION:
Create a function named `generate_fibonacci` that generates a Fibonacci sequence of a specified length `n`. The function should return the sequence as a list of integers. The function must handle cases where `n` is not a positive integer and return an error message in such cases. The function's time complexity should be O(n) and its space complexity should be O(1).
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