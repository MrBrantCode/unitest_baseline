"""
QUESTION:
Write a function named `fibonacci_sequence` that takes one argument `n` and returns a list of the first `n` Fibonacci numbers. Then use this function to generate a matrix of size `matrix_size x matrix_size` where `matrix_size` is given, filled with Fibonacci numbers in row-major order. The function should handle cases where `matrix_size` is a positive integer.
"""

def fibonacci_sequence(n, matrix_size):
    """
    This function generates a list of the first n Fibonacci numbers and returns a matrix of size matrix_size x matrix_size 
    filled with Fibonacci numbers in row-major order.

    Args:
    n (int): The number of Fibonacci numbers to generate.
    matrix_size (int): The size of the matrix.

    Returns:
    list: A 2D list representing the matrix filled with Fibonacci numbers.
    """
    
    # Function to generate a list of Fibonacci numbers till a specific length
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Rewrite the sequence into a matrix
    fib_matrix = [fib_sequence[i:i+matrix_size] for i in range(0, len(fib_sequence), matrix_size)]
    
    return fib_matrix