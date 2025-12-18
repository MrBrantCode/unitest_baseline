"""
QUESTION:
Design a function named `fibonacci_sequence` that generates and displays the Fibonacci sequence using dynamic programming, starting from 1 and ending at the nth term. The function should take an integer `n` as input, have optimized time complexity, and include error handling for invalid input data types or out-of-range input values (n must be a positive integer).
"""

def fibonacci_sequence(n, computed = {0: 0, 1: 1}):
    """
    Generates the nth Fibonacci number using dynamic programming with memoization.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    computed (dict): A dictionary to store previously computed Fibonacci numbers.
    
    Returns:
    int: The nth Fibonacci number.
    """
    
    if n in computed:
        return computed[n]
    else:
        computed[n] = fibonacci_sequence(n-1, computed) + fibonacci_sequence(n-2, computed)
        return computed[n]