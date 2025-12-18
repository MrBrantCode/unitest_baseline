"""
QUESTION:
Create a function named `fibonacci_sum` that calculates the sum of the first 'n' numbers in the Fibonacci sequence. The Fibonacci sequence starts with 1 and 1, and each subsequent term is the sum of the two preceding terms. The input to this function will be the number of terms 'n', and the function should return the sum of the first 'n' terms in the sequence.
"""

def fibonacci_sum(n):
    """
    This function calculates the sum of the first 'n' numbers in the Fibonacci sequence.
    
    Args:
        n (int): The number of terms in the Fibonacci sequence.
    
    Returns:
        int: The sum of the first 'n' terms in the Fibonacci sequence.
    """

    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 1, 1
    
    # Initialize the sum of the Fibonacci sequence
    fib_sum = a + b
    
    # Generate the Fibonacci sequence up to the nth term
    for _ in range(2, n):
        a, b = b, a + b
        fib_sum += b
    
    # Return the sum of the Fibonacci sequence
    return fib_sum