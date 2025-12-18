"""
QUESTION:
Create a function named `even_fibonacci(n)` that takes a positive integer `n` as input and returns a list of even numbers from the Fibonacci sequence up to `n` (inclusive). The function should handle invalid inputs by returning an error message if `n` is not a positive integer.
"""

def even_fibonacci(n):
    # Error handling for non-positive or non-integer inputs.
    if not isinstance(n, int) or n < 1:
        return "Error: Input is not a positive integer."
  
    lst = []  # List to hold the even Fibonacci sequence numbers.
    a, b = 0, 1  # Initialize the first two Fibonacci sequence numbers.
  
    # Iteratively generate the Fibonacci sequence.
    while a <= n:
        # Check if the current Fibonacci number is even.
        if a % 2 == 0:
            lst.append(a)
        
        # Generate the next Fibonacci number.
        a, b = b, a + b
  
    return lst