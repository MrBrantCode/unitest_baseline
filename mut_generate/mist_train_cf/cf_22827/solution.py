"""
QUESTION:
Write a function named `fibonacci(n)` that generates and returns the Fibonacci sequence up to the nth number. The function should use a recursive approach to generate the sequence and handle cases where n is not a positive integer by returning an error message. The input n is expected to be an integer.
"""

def fibonacci(n):
    """
    Generates and returns the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): A positive integer.

    Returns:
        list: A list of integers representing the Fibonacci sequence up to the nth number.
        str: An error message if n is not a positive integer.

    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return "Invalid input. Please enter a positive integer."

    # Recursive function to generate fibonacci sequence
    def fibonacci_recursive(i):
        if i <= 1:
            return i
        else:
            return fibonacci_recursive(i-1) + fibonacci_recursive(i-2)

    # Generate fibonacci sequence
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(fibonacci_recursive(i))
    return fib_sequence